import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import re
from email.utils import formataddr

# URL of the PHP script
url = "https://ibeeanalytics.com/newsletter/testing.php"

# Send a GET request to the PHP script
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    emails = [[item['usr_id'], item['email'], item['count']] for item in data]

else:
    print("Failed to retrieve data:", response.status_code)

# SMTP server configuration
SMTP_SERVER = 'sg2plzcpnl505626.prod.sin2.secureserver.net'  
SMTP_PORT = 25
SENDER_NAME = 'iBee Analytics Newsletter'
SENDER_EMAIL = 'newsletter@ibeeanalytics.com'  
SENDER_PASSWORD = 'sM6W6z+#cjju'

# List of recipients (example list, replace with your actual recipients)

# Email content
subject = "💎 $3,500 Gift Voucher Could Be Yours – Don’t Miss Out!" 

# Throttling settings
emails_per_batch = 10  # Number of emails to send in one batch
sleep_time_between_batches = 10  # Time to sleep between batches (in seconds)

# Create the SMTP session
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# Log file
log_file = open("email_log.txt", "w")

# Send emails in batches
for i in range(0, len(emails), emails_per_batch):
    batch = emails[i:i + emails_per_batch]
    for recipient in batch:
        try:
            html_content = """   <!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>iBee Analytics - Unlock Growth &amp; Opportunities</title>
    <style type="text/css">
        body { margin: 0; padding: 0; width: 100%; min-width: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
        table { border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
        img { border: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }
        a { text-decoration: none; color: #007bff; }
        /* Responsive styles */
        @media only screen and (max-width: 600px) {
            .email-container { width: 100% !important; margin: 0 auto !important; }
            .section-padding { padding: 15px !important; }
            .logo { max-width: 250px !important; }
            .article-img { width: 100% !important; height: auto !important; }
            .winner-image-group { flex-direction: column; }
            .winner-image-item { width: 100% !important; max-width: none !important; }
            .product-gif { width: 100% !important; height: auto !important; }
        }
    </style>
</head>
<body style="margin: 0; padding: 0; width: 100%; min-width: 100%;">
    <table border="0" cellpadding="0" cellspacing="0" class="email-container" role="presentation" style="width: 100%; max-width: 700px; margin: 30px auto; background-color: #f8f8f8; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); overflow: hidden;" width="100%">
        <tr>
            <td align="center" class="header-bg" style="background-color: #eff1f4; padding: 25px 20px; text-align: center;">
                <a href="https://ibeeanalytics.com" style="text-decoration: none;" target="_blank">
                    <img alt="iBee Analytics" class="logo" src="https://ibeeanalytics.com/newsletter/ibeeanalytics_logo.png" style="max-width: 350px; width: 100%; height: auto; display: block; margin: 0 auto;" width="350"/>
                </a>
                <p class="header-links" style="margin-top: 15px; font-size: 0.9em; color: #777; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">
                    <a href="mailto:contact@ibeeanalytics.com" style="color: #0a0a09; margin: 0 10px; text-decoration: none; font-weight: 500;">Email</a> |
                    <a href="https://ibeeanalytics.com" style="color: #0a0a09; margin: 0 10px; text-decoration: none; font-weight: 500;" target="_blank">Website</a>
                </p>
            </td>
        </tr>
        <tr>
            <td align="right" style="padding: 10px 20px 0 20px; background-color: #f2faff;">
              <span style="display: inline-block; background-color: #e14e0f; color: #ffffff; font-size: 13px; font-weight: 600; padding: 6px 12px; border-radius: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                🕒 Read in 3 min
              </span>
            </td>   
          </tr>


        <tr>
            <td class="section-padding section-separator" style="background-color: #f2faff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
              <div class="info-box" style="background-color: #ffffff; padding: 25px; border-radius: 10px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
                <h2 style="font-size: 1.7em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 3px solid #007bff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3; text-align: center;">
                  ✨ Unlock Growth with iBee Analytics ✨
                </h2>
                <p style="font-size: 1em; color: #555555; line-height: 1.6; margin-bottom: 15px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: justify;">
                  Get weekly insights, explore career moves, and earn rewards for sharing!
                </p>

                <div style="background-color: #fff9ed; border: 1px solid #ffdebc; border-radius: 8px; padding: 15px; margin-bottom: 20px; text-align: center;">
                    <p style="font-size: 1.05em; color: #cc7000; font-weight: bold; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0;">
                        🎁 Limited-Time Offer! Refer friends and you could win a <strong>$3,500 Gift Voucher</strong>. Capture your adventures while growing the iBee community.
                    </p>
                  </div>
              </div>
            </td>
          </tr>

<tr>
  <td class="section-padding section-separator" style="background-color: #f2faff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
    <div class="info-box" style="background-color: #ffffff; padding: 25px; border-radius: 10px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
      <h2 style="font-size: 1.8em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-bottom: 3px solid #007bff; padding-bottom: 10px; text-align: center; line-height: 1.3;">
        MARKETS 📈
        <br>
        <span style="font-size: 0.6em; font-weight: normal; color: #555;">A snapshot of recent market highlights you won't want to miss!</span>
      </h2>

      <table role="presentation" cellpadding="10" cellspacing="0" width="100%" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1em; color: #333; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.05);">
        <thead style="background-color: #e6f7ff; color: #0056b3;">
          <tr>
            <th align="left" style="padding: 12px 10px; font-weight: 700; border-bottom: 2px solid #b3d9ff; font-size: 1.1em;">Company (Ticker)</th>
            <th align="right" style="padding: 12px 10px; font-weight: 700; border-bottom: 2px solid #b3d9ff; font-size: 1.1em;">Last Price</th>
            <th align="right" style="padding: 12px 10px; font-weight: 700; border-bottom: 2px solid #b3d9ff; font-size: 1.1em;">Change</th>
            <th align="right" style="padding: 12px 10px; font-weight: 700; border-bottom: 2px solid #b3d9ff; font-size: 1.1em;">% Change</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>BigBear.ai Holdings, Inc</strong> (BBAI)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$7.56</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.91</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+13.68% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>NVIDIA Corporation</strong> (NVDA)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$157.25</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+3.95</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+2.58% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Intel Corporation</strong> (INTC)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$21.88</td>
            <td align="right" style="color: #dc3545; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">-0.97</td>
            <td align="right" style="color: #dc3545; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">-4.25% ⬇️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Lucid Group, Inc.</strong> (LCID)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$2.05</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.02</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.99% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Ford Motor Company</strong> (F)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$11.77</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.42</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+3.70% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Tesla, Inc.</strong> (TSLA)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$315.65</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+14.94</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+4.97% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Robinhood Markets, Inc. Cla...</strong> (HOOD)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$97.98</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+5.65</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+6.12% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Vale S.A. Sponsored ADR</strong> (VALE)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$10.28</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.46</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+4.68% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px; border-bottom: 1px solid #f0f0f0;"><strong>Cipher Mining Inc</strong> (CIFR)</td>
            <td align="right" style="padding: 10px; border-bottom: 1px solid #f0f0f0;">$5.68</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+0.78</td>
            <td align="right" style="color: #28a745; font-weight: bold; padding: 10px; border-bottom: 1px solid #f0f0f0;">+15.92% ⬆️</td>
          </tr>
          <tr>
            <td style="padding: 10px;"><strong>Centene Corporation</strong> (CNC)</td>
            <td align="right" style="padding: 10px;">$33.78</td>
            <td align="right" style="color: #dc3545; font-weight: bold; padding: 10px;">-22.87</td>
            <td align="right" style="color: #dc3545; font-weight: bold; padding: 10px;">-40.37% ⬇️</td>
          </tr>
        </tbody>
      </table>

      <p style="font-size: 0.9em; color: #6c757d; margin-top: 18px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: left; background-color: #f0f8ff; padding: 8px; border-left: 4px solid #007bff; border-radius: 4px;">
        Data last updated Jul 2 at 8:00:00 PM ET. Trade volume is from Nasdaq, NYSE, and NYSE American and includes stocks with a prior close of $2 or higher.
        <br>
        <strong>Source: CNN Markets</strong>
        <a href="https://edition.cnn.com/markets" style="color: #007bff; text-decoration: none; font-weight: bold;"> &ndash; Explore More Market Insights Here! 📈</a>
      </p>
    </div>
  </td>
</tr>

<tr>
  <td class="section-padding section-separator" style="background-color: #ffffff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
    <h2 style="font-size: 1.7em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-bottom: 3px solid #007bff; padding-bottom: 10px; text-align: center;">
      ✨ Your Edge Starts Here! 
      <br>
      <span style="font-size: 0.6em; font-weight: normal; color: #555;">Unlock Exclusive Insights & Opportunities</span>
    </h2>
    <p style="font-size: 1em; color: #555555; line-height: 1.6; margin-bottom: 15px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: justify;">
      This isn't just a newsletter it's your strategic advantage. Dive in for what truly matters:
    </p>
    <ul style="font-size: 1em; color: #333333; line-height: 1.8; margin-bottom: 15px; padding-left: 25px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
      <li style="margin-bottom: 8px;">
         Featured Insights: Expert analysis on tech and industry shifts.
      </li>
      <li style="margin-bottom: 8px;">
         ChatGPT Prompts: Master AI, supercharge your workflow.
      </li>
      <li style="margin-bottom: 8px;">
         Tech Opportunities: Discover high-demand roles for your next career move.
      </li>
      <li style="margin-bottom: 8px;">
         iBee Swag: Learn how to win by sharing our content!
      </li>
    </ul>
    <p style="font-size: 1em; color: #1b1b1b; line-height: 1.6; margin-bottom: 0; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: bold;">
      Get informed, get inspired, get ahead. Read on!
    </p>
  </td>
</tr>
<tr>
    <td class="section-padding section-separator" style="background-color: #f2faff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
      <h2 style="font-size: 1.8em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 15px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-bottom: 3px solid #007bff; padding-bottom: 10px; text-align: center; line-height: 1.3;">
        💡 Featured Insights: Dive Deeper! 
        <br>
      </h2>
  
      <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px; overflow: hidden;" width="100%">
        <tr>
          <td class="article-img-td" style="padding: 0;">
            <img alt="Snap Unveils Sleeker AR Glasses" class="article-img" src="https://ibeeanalytics.com/newsletter/july-04-1-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
          </td>
        </tr>
        <tr>
          <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-top: 3px solid #007bff;">
            <div class="article-title" style="font-size: 1.3em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">Snap Unveils Sleeker AR Glasses</div>
            <p class="article-summary" style="font-size: 1.0em; color: #1b1b1b; line-height: 1.7; margin-bottom: 0; margin-top: 0; text-align: justify; text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.05);">
              Snap Inc. is preparing to reshape the augmented reality landscape with the upcoming launch of its smaller, lighter <strong>Specs smartglasses in 2026</strong>. These next-generation Spectacles promise a sleeker design and enhanced performance, making AR more accessible and stylish for everyday users. Building on years of experimentation and feedback, Snap aims to create a truly wearable tech experience that blends seamlessly with daily life. With improved display technology, comfort, and functionality, this release could mark a <strong>major milestone in mainstream AR adoption</strong>. Stay tuned for more on what’s coming.
            </p>
          </td>
        </tr>
      </table>
  
      <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px; overflow: hidden;" width="100%">
        <tr>
          <td class="article-img-td" style="padding: 0;">
            <img alt="AeroVironment Shares Tumble 7%" class="article-img" src="https://ibeeanalytics.com/newsletter/july-04-2-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
          </td>
        </tr>
        <tr>
          <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-top: 3px solid #007bff;">
            <div class="article-title" style="font-size: 1.3em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">AeroVironment Shares Tumble 7%</div>
            <p class="article-summary" style="font-size: 1.0em; color:#1b1b1b; line-height: 1.7; margin-bottom: 0; margin-top: 0; text-align: justify; text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.05);">
              AeroVironment Inc. (NASDAQ: AVAV) saw its stock tumble roughly <strong>7% today</strong> after announcing an ambitious <strong>$1.35 billion capital‑raising effort</strong>. The defense‑focused drone specialist plans to issue $750 million in common shares along with $600 million in convertible senior notes maturing in 2030. Proceeds will be channeled primarily toward repaying existing debt, with any surplus funding allocated for expanding manufacturing capacity and general corporate needs. Despite the dip, AVAV has delivered an <strong>impressive 85% gain this year</strong>, pushing its market cap close to $13 billion, as investors continue to weigh near‑term dilution against long‑term growth prospects.
            </p>
          </td>
        </tr>
      </table>
  
      <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="margin-bottom: 0; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden;" width="100%">
        <tr>
          <td class="article-img-td" style="padding: 0;">
            <img alt="Caring Mom’s Medicaid at Stake" class="article-img" src="https://ibeeanalytics.com/newsletter/july-04-3-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
          </td>
        </tr>
        <tr>
          <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border-top: 3px solid #007bff;">
            <div class="article-title" style="font-size: 1.3em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">Caring Mom’s Medicaid at Stake</div>
            <p class="article-summary" style="font-size: 1.0em; color: #1b1b1b; line-height: 1.7; margin-bottom: 0; margin-top: 0; text-align: justify; text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.05);">
              In a significant policy shift, some Medicaid recipients, including family caregivers, may soon be required to <strong>prove employment to retain their benefits</strong>. One such affected individual is a devoted mother caring full-time for her disabled adult son. Proposed work requirements, aimed at encouraging employment among able-bodied adults, risk overlooking the unpaid labor of caregivers whose contributions are both critical and compassionate. This development raises urgent concerns about the <strong>value placed on caregiving</strong>, the accessibility of Medicaid, and the unintended harm such policies could inflict on families relying on these vital supports. Here’s what you need to know.
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>    
  <tr>
    <td class="section-padding section-separator" style="background-color: #f2faff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
      <div class="info-box" style="background-color: #ffffff; padding: 25px; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
        <h2 style="font-size: 1.7em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 3px solid #007bff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3; text-align: center;">
          💡 Master AI: Boost Your Productivity with ChatGPT Prompts
          <br>
          <span style="font-size: 0.6em; font-weight: normal; color: #555;">Unlock Powerful Capabilities for Your Workflow</span>
        </h2>
        <div class="prompt-item" style="background-color: #fcfcfc; padding: 18px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); margin-bottom: 15px; line-height: 1.6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
          <strong style="color: #007bff; font-size: 1.1em;">Unlock Your Potential: 5 Powerful ChatGPT Prompts for Building Multimodal AI Chatbots</strong>
          <ul style="list-style-type: none; padding-left: 0; margin-top: 15px; margin-bottom: 0;">
            <li style="margin-bottom: 10px; position: relative; padding-left: 15px; text-align: justify; font-size: 0.98em; color: #333; font-weight: normal;">
              <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Image Processing Chatbot:</b> Design a chatbot that accepts user-uploaded images, analyzes them using AI (e.g., object detection, OCR, face recognition), and provides meaningful results. Outline the best tools (like OpenCV, TensorFlow, or CLIP), model choices, and how to integrate image input into the frontend using React or Python.</span>
            </li>
            <li style="margin-bottom: 10px; position: relative; padding-left: 15px; text-align: justify; font-size: 0.98em; color: #333; font-weight: normal;">
              <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Voice-Enabled Assistant:</b> Build a voice-interactive chatbot using Web Speech API or Whisper by OpenAI. Guide me through converting speech to text and responding with AI-generated voice. Include sample code snippets for browser-based implementation.</span>
            </li>
            <li style="margin-bottom: 10px; position: relative; padding-left: 15px; text-align: justify; font-size: 0.98em; color: #333; font-weight: normal;">
              <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>AI Image Generation Bot:</b> Create a chatbot that can generate AI images based on user prompts using Stable Diffusion or DALL·E. Provide full-stack guidance (frontend for prompt input + backend integration with API). Also explain how to manage generated image storage and display.</span>
            </li>
            <li style="margin-bottom: 10px; position: relative; padding-left: 15px; text-align: justify; font-size: 0.98em; color: #333; font-weight: normal;">
              <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Research Assistant Chatbot:</b> Develop a chatbot that performs real-time web research on a given topic, extracts key insights, and summarizes them. Show how to use tools like Python's serpapi, BeautifulSoup, or OpenAI’s Web Browse capabilities. Suggest prompt engineering strategies to get better search results.</span>
            </li>
            <li style="margin-bottom: 0; position: relative; padding-left: 15px; text-align: justify; font-size: 0.98em; color: #333; font-weight: normal;">
              <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Thinking / Reasoning AI Bot:</b> Create a chatbot that mimics human-like step-by-step logical reasoning. Use chain-of-thought prompting with OpenAI’s GPT models. Show example code for embedding this logic into a chatbot that helps programmers debug code or solve algorithmic problems step by step.</span>
            </li>
          </ul>
        </div>
      </div>
    </td>
  </tr>     
<tr>
            <td class="section-padding section-separator" style="background-color: #f2faff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
                <div class="info-box" style="background-color: #ffffff; padding: 25px; border-radius: 10px; margin-bottom: 25px; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
                    <h2 style="font-size: 1.7em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 3px solid #007bff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3; text-align: center;">
                        🏆 Recent Winners! Congratulations! 🎉
                    </h2>
                    <table class="winner-card" role="presentation" style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden;" width="100%" cellspacing="0" cellpadding="0">
                        <tr>
                            <td style="padding: 0;">
                                <h3 style="margin: 0; font-size: 1.15em; color: #00008b; padding: 15px 20px; border-bottom: 1px solid #eeeeee; background-color: #fdfdfd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-height: 1.3;">Customized Electric Bike Winners</h3>
                                <div class="winner-content" style="padding: 20px; text-align: center;">
                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                        <tr>
                                            <td align="center" valign="top" style="padding: 10px;">
                                                <img alt="Customized Electric Bike Winners" src="https://ibeeanalytics.com/newsletter/july-04-4-2025.jpg" style="width: 100%; max-width: 200px; height: auto; border-radius: 8px; display: block;" width="200"/>
                                                <p style="font-size: 0.95em; color: #555555; margin: 5px 0 0 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Maya Ellison</p>
                                            </td>
                                            <td align="center" valign="top" style="padding: 10px;">
                                                <img alt="Customized Electric Bike Winners" src="https://ibeeanalytics.com/newsletter/july-04-5-2025.jpg" style="width: 100%; max-width: 200px; height: auto; border-radius: 8px; display: block;" width="200"/>
                                                <p style="font-size: 0.95em; color: #555555; margin: 5px 0 0 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Ethan Brooks</p>
                                            </td>
                                        </tr>
                                    </table>
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
            </td>
        </tr>
        <tr>
            <td class="section-padding" style="background-color: #f2faff; padding: 25px 20px;">
                <div class="level-up-container" style="background-color: #ffffff; padding: 25px; border-radius: 10px; text-align: center; box-shadow: 0 6px 15px rgba(0,0,0,0.1);">
                    <h2 style="font-size: 1.7em; font-weight: bold; color: #1b1b1b; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 3px solid #007bff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3; text-align: center;">
                        🎁 Unlock Exclusive iBee Swag: Share & Earn! 🚀
                    </h2>
                    <p style="font-size: 0.95em; margin-bottom: 20px; color: #555555; margin-top: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">
                        Share the iBee Analytics newsletter with your network and earn fantastic free iBee swag!
                    </p>
                    <div style="text-align: center; margin-bottom: 25px;">
                        <img alt="iBee Swag Products" class="product-gif" src="https://ibeeanalytics.com/newsletter/product.gif" style="width: 100%; max-width: 300px; height: auto; border-radius: 10px; display: inline-block;" />
                    </div>
                    <table border="0" cellpadding="0" cellspacing="0" class="rewards-table" role="presentation" style="width: 100%; margin-top: 20px; border-collapse: separate; border-spacing: 0 10px;" width="100%">
                        <tr>
                            <td colspan="2" style="text-align: center; background-color: transparent; box-shadow: none; padding-bottom: 5px; padding-top: 0; font-size: 1.1em; line-height: 1.5;">
                                <strong style="color: #007bff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">🎉 Your Rewards Await! 🎉</strong>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">5 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Stickers</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">10 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Pen Stand</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">15 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Tote</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">25 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Coffee Mug</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">50 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Mystery Box</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <strong style="color: #333333;">100 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #fcfcfc; padding: 12px 15px; border-radius: 8px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; border: 1px solid #eee;">
                                <span style="color: #555555;">Work Table Setup</span>
                            </td>
                        </tr>                    </table>
                    <p class="referral-info" style="font-size: 0.95em; margin-top: 25px; color: #555555; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Your referral count: <span style="font-weight: bold;">"""+recipient[2]+"""</span></p>
                    <div style="text-align: center; margin-top: 20px;">
                        <a class="cta-button" href="https://ibeeanalytics.com/check-letter.php?us="""+recipient[0]+"""' style="display: inline-block; padding: 12px 25px; background-color: #007bff; color: #ffffff !important; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 1em; letter-spacing: 0.5px; mso-hide: all; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Share Now &amp; Earn Rewards!</a>
                    </div>
                    <p class="referral-link-text" style="font-size: 0.85em; color: #777777; margin-top: 15px; display: block; word-break: break-all; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Or copy &amp; paste your referral link: <a href="https://ibeeanalytics.com/check-letter.php?us="""+recipient[0]+"""' style="color: #777777; text-decoration: underline;">https://ibeeanalytics.com/check-letter.php?us="""+recipient[0]+"""</a></p>                </div>
            </td>
        </tr>
        <tr>
            <td class="footer-bg" style="text-align: center; padding: 25px 20px; font-size: 0.85em; background-color: #eff1f4; color: #333333; border-radius: 0 0 10px 10px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">
                    <div class="social-links" style="margin-bottom: 20px; font-size: 0; text-align: center;">
                    <a href="https://www.facebook.com/profile.php?id=61552503802057" style="display: inline-block; margin: 0 5px;">
                        <img alt="iBee Analytics Facebook" src="https://ibeeanalytics.com/newsletter/fb.png" style="background-color: rgba(0, 0, 0, 0.1); border-radius: 3px; vertical-align: middle;"/>
                    </a>
                    <a href="https://twitter.com/iBee_Analytics" style="display: inline-block; margin: 0 5px;">
                        <img alt="iBee Analytics Twitter" src="https://ibeeanalytics.com/newsletter/twi.png" style="background-color: rgba(0, 0, 0, 0.1); border-radius: 3px; vertical-align: middle;"/>
                    </a>
                    <a href="https://www.instagram.com/ibee_analytics/" style="display: inline-block; margin: 0 5px;">
                        <img alt="iBee Analytics Instagram" src="https://ibeeanalytics.com/newsletter/ins.png" style="background-color: rgba(0, 0, 0, 0.1); border-radius: 3px; vertical-align: middle;"/>
                    </a>
                    <a href="https://www.linkedin.com/company/ibee-analytics" style="display: inline-block; margin: 0 5px;">
                        <img alt="iBee Analytics LinkedIn" src="https://ibeeanalytics.com/newsletter/link.png" style="background-color: rgba(0, 0, 0, 0.1); border-radius: 3px; vertical-align: middle;"/>
                    </a>
                </div>
                <p style="margin: 0; padding: 0; color: #555555; font-size: 0.85em; line-height: 1.5;">
                    © 2025 iBee Analytics. All rights reserved.<br/>
                    <a href="https://ibeeanalytics.com/privacy_policy.php?pp=1" style="color: #007bff; text-decoration: none;" target="_blank">Privacy Policy</a> 
                </p>
            </td>
        </tr>
    </table>
</body>
</html>









 
 
























                   """
            msg = MIMEMultipart()
            msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
            msg['To'] = recipient[1]
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(html_content, 'html'))

            # Send the email
            server.sendmail(SENDER_EMAIL, recipient[1], msg.as_string())
            log_file.write(f"Email sent to {recipient[1]} (User ID: {recipient[0]})\n")
            print(f"Email sent to {recipient[1]} (User ID: {recipient[0]})")

        except Exception as e:
            # log_file.write(f"Failed to send email to {recipient[1]}-{recipient[0]} {e}\n")
            # print(f"Failed to send email to {recipient[1]}-{recipient[0]} {e}")
            max_retries = 5
            retry_count = 0
            while retry_count < max_retries:
                try:
                    # Create the SMTP session
                    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                    server.starttls()
                    server.login(SENDER_EMAIL, SENDER_PASSWORD)
                    break
                except smtplib.SMTPException as e:
                    print(f"Failed to connect to SMTP server: {e}")
                    print(f"Retrying ({retry_count+1}/{max_retries}) in 5 seconds...")
                    time.sleep(5)
                    retry_count += 1
            if retry_count == max_retries:
                print("Failed to connect to SMTP server after maximum retries. Exiting.")
                sys.exit(1)

    # Sleep between batches
    print(f"Sleeping for {sleep_time_between_batches} seconds or press Ctrl C")
    time.sleep(sleep_time_between_batches)

# Terminate the SMTP session
server.quit()

log_file.close()

print("All emails sent successfully! Check the log file for details.")
# check subject 
# check add page
# check referral section link
# send mail automation
