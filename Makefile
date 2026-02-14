.PHONY: send-mib

# Usage: make send-mib DATE=2026-02-14 ISSUE=1
send-mib:
	@python3 scripts/send_mib.py --date $(DATE) --issue $(ISSUE)
