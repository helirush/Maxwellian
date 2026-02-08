#!/bin/bash
# ═══════════════════════════════════════════════════════════
# Audit Sensitive Content Script
# Identifies files that should be moved to Private/ directory
# ═══════════════════════════════════════════════════════════

echo "════════════════════════════════════════════════════════"
echo "Unity Knowledge Base - Sensitive Content Audit"
echo "════════════════════════════════════════════════════════"
echo ""

# Customer name patterns
CUSTOMER_PATTERNS="Foster|Farms|Livingston|Cherry|FosterFarms"

# Financial patterns
FINANCIAL_PATTERNS="\$[0-9,]+|invoice|quote|contract|pricing|ROI.*[0-9]"

# Credential patterns
CREDENTIAL_PATTERNS="API.*KEY.*=|password|credential|secret.*="

echo "Scanning for customer-specific references..."
echo "────────────────────────────────────────────────────────"
grep -r -l "$CUSTOMER_PATTERNS" Memory/ 2>/dev/null | while read file; do
    echo "  🔴 Customer ref: $file"
done

echo ""
echo "Scanning for financial details..."
echo "────────────────────────────────────────────────────────"
grep -r -l -E "$FINANCIAL_PATTERNS" Memory/ 2>/dev/null | while read file; do
    echo "  💰 Financial: $file"
done

echo ""
echo "Scanning for credentials..."
echo "────────────────────────────────────────────────────────"
grep -r -l -E "$CREDENTIAL_PATTERNS" Memory/ 2>/dev/null | while read file; do
    echo "  🔐 Credential: $file"
done

echo ""
echo "════════════════════════════════════════════════════════"
echo "RECOMMENDATION:"
echo "════════════════════════════════════════════════════════"
echo "Files marked above should be reviewed. Consider:"
echo "  1. Generalize examples (replace 'Foster Farms' with 'Customer A')"
echo "  2. Move to ../Private/CustomerFiles/ if customer-specific"
echo "  3. Redact financial details or move to ../Private/Financial/"
echo "  4. Never commit actual credentials - keep references only"
echo ""
echo "To move files safely:"
echo "  mkdir -p ../Private/CustomerFiles"
echo "  mv Memory/filename.md ../Private/CustomerFiles/"
echo ""
