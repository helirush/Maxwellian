#!/usr/bin/env python3
import os, sys, argparse, smtplib, yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from datetime import datetime

DEFAULT_BASE_DIR = os.path.join('Unity', 'Briefs')

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def build_subject(date_str, issue):
    # YYMMDD.issue
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    ymd = dt.strftime('%y%m%d')
    return f'Maxwellian Intelligence Brief {ymd}.{issue}'

def send_email(smtp_host, smtp_port, username, password, from_name, from_email, to_list, cc_list, subject, html_body, attachment_text, attachment_name):
    msg = MIMEMultipart('mixed')
    msg['From'] = formataddr((from_name, from_email))
    msg['To'] = ', '.join(to_list)
    if cc_list:
        msg['Cc'] = ', '.join(cc_list)
    msg['Subject'] = subject

    alt = MIMEMultipart('alternative')
    alt.attach(MIMEText('This email contains HTML content. Please use an HTML-capable client.', 'plain'))
    alt.attach(MIMEText(html_body, 'html'))
    msg.attach(alt)

    attach = MIMEText(attachment_text, 'plain')
    attach.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    msg.attach(attach)

    recipients = to_list + (cc_list or [])
    with smtplib.SMTP_SSL(smtp_host, int(smtp_port)) as server:
        server.login(username, password)
        server.sendmail(from_email, recipients, msg.as_string())

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Send Maxwellian Intelligence Brief from saved files')
    ap.add_argument('--date', required=True, help='Date YYYY-MM-DD')
    ap.add_argument('--issue', default='1')
    ap.add_argument('--base-dir', default=DEFAULT_BASE_DIR)
    ap.add_argument('--config', default=os.path.join('config','oliver_mib_distribution.yaml'))
    ap.add_argument('--to', nargs='*', help='Override TO list')
    ap.add_argument('--cc', nargs='*', help='Override CC list')
    args = ap.parse_args()

    cfg = load_config(args.config)
    from_name = cfg['from_name']
    from_email = cfg['from_email']
    to_list = args.to or cfg['to']
    cc_list = args.cc or cfg.get('cc', [])

    brief_dir = os.path.join(args.base_dir, args.date)
    html_path = os.path.join(brief_dir, 'brief.html')
    txt_path = os.path.join(brief_dir, 'AI_Partner.txt')

    if not (os.path.exists(html_path) and os.path.exists(txt_path)):
        sys.exit(f'Missing files in {brief_dir}. Expect brief.html and AI_Partner.txt')

    with open(html_path, 'r', encoding='utf-8') as f:
        html_body = f.read()
    with open(txt_path, 'r', encoding='utf-8') as f:
        txt_body = f.read()

    subject = build_subject(args.date, args.issue)

    smtp_host = os.environ.get('OLIVER_SMTP_HOST', 'smtpout.secureserver.net')
    smtp_port = os.environ.get('OLIVER_SMTP_PORT', '465')
    username = os.environ['OLIVER_SMTP_USERNAME']
    password = os.environ['OLIVER_SMTP_PASSWORD']

    send_email(smtp_host, smtp_port, username, password, from_name, from_email, to_list, cc_list, subject, html_body, txt_body, f'Maxwellian_Intelligence_Brief_{args.date}_AI_Partner.txt')
    print(f'Sent {subject} to {len(to_list)} TO and {len(cc_list)} CC from {from_email}')
