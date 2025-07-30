import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import re
from email.utils import formataddr

# URL of the PHP script
url = "https://ibeeanalytics.com/newsletter/setcout.php"

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

# Email content add new subject
subject = "🚀 Grab Your Chance - iPhone 16 Pro Max Could Be Yours!"

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
            html_content = """      <!DOCTYPE html>
                








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
            <td class="section-padding section-separator" style="background-color: #ffffff; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
                <h2 class="intro-title" style="font-size: 1.6em; font-weight: 700; color: #222222; margin-top: 0; margin-bottom: 15px; line-height: 1.3; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Unlock Growth with iBee Analytics: Your Weekly Dose of Insights &amp; Opportunities</h2>
                <p class="intro-text" style="font-size: 1em; color: #555555; line-height: 1.7; margin-bottom: 15px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: justify;">
                    Stay ahead in the digital landscape with our expert analysis, discover new career paths, and earn exciting rewards by sharing with your network!
                </p>
                <div class="hero-offer" style="background-color: #fff9ed; border: 1px solid #ffdebc; border-radius: 8px; padding: 15px; margin-bottom: 20px; text-align: center;">
                    <p class="hero-offer-text" style="font-size: 1.1em; color: #cc7000; font-weight: bold; line-height: 1.5; margin-bottom: 10px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                        Limited-Time Offer! Refer friend s and you could Win an iPhone 16 Pro Max Capture your adventures while growing the iBee community.
                    </p>
                </div>
                <p class="intro-text" style="margin-bottom: 0; font-size: 1em; color: #555555; line-height: 1.7; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: justify;">
                    Drive Measurable Results with AI-Powered Marketing. iBee Analytics delivers cutting-edge SEO and cloud solutions, designed to elevate your online presence and achieve tangible business growth. Let's transform your digital strategy!
                </p>
            </td>`
        </tr>
        <tr>
            <td class="section-padding section-separator" style="background-color: #f8f8f8; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
                <h2 style="font-size: 1.4em; font-weight: bold; color: #333333; margin-top: 0; margin-bottom: 25px; padding-bottom: 10px; border-bottom: 2px solid #dddddd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3;">
                    Featured Insights: Grow Your Knowledge Base
                </h2>
                <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 25px; overflow: hidden;" width="100%">
                    <tr>
                        <td class="article-img-td" style="padding: 0;">
                            <img alt="Hackathon Tackles Defense Challenges" class="article-img" src="https://ibeeanalytics.com/newsletter/june-27-1-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
                        </td>
                    </tr>
                    <tr>
                        <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                            <div class="article-title" style="font-size: 1.25em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">Hackathon Tackles Defense Challenges</div>
                            <p class="article-summary" style="font-size: 1.0em; color: #1b1b1b; line-height: 1.6; margin-bottom: 0; margin-top: 0; text-align: justify;">
                                In a dynamic push to enhance military strength, Europe is accelerating its investment in cutting-edge defense technologies. Recently, hackathon teams from across the continent have come together, racing against the clock to develop innovative solutions addressing pressing defense challenges. These collaborative tech competitions spotlight the growing role of agile innovation in modern warfare, with startups, researchers, and defense experts uniting to deliver rapid, practical breakthroughs. As Europe strengthens its military capabilities amid shifting geopolitical landscapes, these hackathons serve as a crucial platform driving technological advancements and strategic readiness.
                            </p>
                        </td>
                    </tr>
                </table>
                <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 25px; overflow: hidden;" width="100%">
                    <tr>
                        <td class="article-img-td" style="padding: 0;">
                            <img alt="AI’s Role in Modern Medicine" class="article-img" src="https://ibeeanalytics.com/newsletter/june-27-2-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
                        </td>
                    </tr>
                    <tr>
                        <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                            <div class="article-title" style="font-size: 1.25em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">AI’s Role in Modern Medicine</div>
                            <p class="article-summary" style="font-size: 1.0em; color:#1b1b1b; line-height: 1.6; margin-bottom: 0; margin-top: 0; text-align: justify;">
                               Artificial Intelligence (AI) is rapidly transforming the landscape of modern medicine, offering the potential to revolutionize diagnostics, treatment planning, drug discovery, and patient care. From AI-powered imaging tools that detect diseases earlier to predictive analytics that support clinical decisions, the promise of AI is undeniable. However, this technological leap comes with significant challenges, including ethical concerns, data privacy issues, bias in algorithms, and the need for rigorous validation. As the medical field embraces innovation, it must also navigate these complexities to ensure that AI serves as a tool for enhancing not replacing human expertise in healthcare.
                            </p>
                        </td>
                    </tr>
                </table>
                <table border="0" cellpadding="0" cellspacing="0" class="article-block" role="presentation" style="margin-bottom: 0; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden;" width="100%">
                    <tr>
                        <td class="article-img-td" style="padding: 0;">
                            <img alt="Americans Endure Extreme Heat" class="article-img" src="https://ibeeanalytics.com/newsletter/june-27-3-2025.jpg" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; display: block;" width="700"/>
                        </td>
                    </tr>
                    <tr>
                        <td class="article-text-area" style="padding: 20px; text-align: justify; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                            <div class="article-title" style="font-size: 1.25em; font-weight: 700; color: #333333; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">Americans Endure Extreme Heat</div>
                            <p class="article-summary" style="font-size: 1.0em; color: #1b1b1b; line-height: 1.6; margin-bottom: 0; margin-top: 0; text-align: justify;">
                                As a relentless heat wave sweeps across the United States, Americans are grappling with record-breaking temperatures that have turned everyday life into a battle against the elements. From sweltering city streets to scorched rural towns, the extreme heat is pushing infrastructure, health systems, and personal resilience to their limits. This edition of our newsletter captures the human side of the crisis through powerful photos of people seeking relief, adapting, and enduring. Whether it's families crowding into cooling centers or kids finding solace in public fountains, these images reveal the urgent need for both compassion and climate action.


                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td class="section-padding section-separator" style="background-color: #f8f8f8; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
                <div class="info-box" style="background-color: #f0f0f0; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
                    <h2 style="font-size: 1.4em; font-weight: bold; color: #333333; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 2px solid #dddddd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3;">
                        Stay Ahead: Actionable Insights &amp; ChatGPT Prompts to Boost Your Productivity
                    </h2>
                    <div class="prompt-item" style="background-color: #ffffff; padding: 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); margin-bottom: 12px; line-height: 1.6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                        <strong style="color: #007bff;">Unlock Your Potential:5 Powerful ChatGPT Prompts to Create Engaging LinkedIn Blogs on AI & Technology</strong>
                        <ul style="list-style-type: none; padding-left: 0; margin-top: 10px; margin-bottom: 0;">
                            <li style="margin-bottom: 8px; position: relative; padding-left: 15px; text-align: justify;">
                                <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>The Future of AI in Everyday Life: Visualizing Tomorrow:</b> Generate a LinkedIn blog post that explores how artificial intelligence will be integrated into daily life by 2035. Include engaging visuals or graphic ideas showing AI in homes, workplaces, transport, and healthcare. Use a forward-looking tone with accessible language for a professional audience.</span>
                            </li>
                            <li style="margin-bottom: 8px; position: relative; padding-left: 15px; text-align: justify;">
                                <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>How AI is Reshaping the Modern Workplace:</b> Write a LinkedIn blog post discussing the impact of AI technologies on office productivity, automation, and remote collaboration. Include infographic-style graphic ideas comparing traditional vs AI-enhanced workflows. Target professionals and business leaders.</span>
                            </li>
                            <li style="margin-bottom: 8px; position: relative; padding-left: 15px; text-align: justify;">
                                <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>AI vs Human Intelligence: A Visual Deep Dive:</b> Create a thought-provoking LinkedIn blog post that compares artificial and human intelligence. Include suggested graphics like brain-AI circuitry comparisons, decision-making flowcharts, and learning models. Keep it professional, analytical, and visually engaging.</span>
                            </li>
                            <li style="margin-bottom: 8px; position: relative; padding-left: 15px; text-align: justify;">
                                <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Tech Trends 2025: The Rise of Ethical AI:</b> Write a blog for LinkedIn focusing on the ethical challenges of AI in 2025. Include ideas for impactful illustrations or charts such as an ‘AI Ethics Checklist’ or ‘Responsible AI Flow’. Keep the tone informative and suitable for tech-savvy professionals.</span>
                            </li>
                            <li style="margin-bottom: 0; position: relative; padding-left: 15px; text-align: justify;">
                                <span style="position: absolute; left: 0; top: 0; color: #007bff;">•</span> <span><b>Demystifying Generative AI: From Prompt to Pixel:</b> Generate a LinkedIn blog post explaining how generative AI works from text prompts to image or video creation. Include suggested visuals like a pipeline diagram, before-and-after samples, or prompt-to-result timelines. Make it educational and shareable for tech content creators.</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </td>
        </tr>
        <tr>
            <td class="section-padding section-separator" style="background-color: #f8f8f8; padding: 25px 20px; border-bottom: 1px solid #e9e9e9;">
                <div class="info-box" style="background-color: #f0f0f0; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
                    <h2 style="font-size: 1.4em; font-weight: bold; color: #333333; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 2px solid #dddddd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3;"> Recent Winners! Congratulations! </h2>
                    <table class="winner-card" role="presentation" style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); overflow: hidden;" width="100%" cellspacing="0" cellpadding="0">
                        <tr>
                            <td style="padding: 0;">
                                <h3 style="margin: 0; font-size: 1.15em; color: #00008b; padding: 15px 20px; border-bottom: 1px solid #eeeeee; background-color: #fdfdfd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3;">Blogging Mic Winners</h3>
                                <div class="winner-content" style="padding: 20px; text-align: center;">
                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                        <tr>
                                            <td align="center" valign="top" style="padding: 10px;">
                                                <img alt="Ultra-Luxury Wellness Retreat Kit Winner" src="https://ibeeanalytics.com/newsletter/june-27-4-2025.jpg" style="width: 100%; max-width: 200px; height: auto; border-radius: 8px; display: block;" width="200"/>
                                                <p style="font-size: 0.95em; color: #555555; margin: 5px 0 0 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Mira Solene Veyra</p>
                                            </td>
                                            <td align="center" valign="top" style="padding: 10px;">
                                                <img alt="Ultra-Luxury Wellness Retreat Kit Winner" src="https://ibeeanalytics.com/newsletter/june-27-5-2025.jpg" style="width: 100%; max-width: 200px; height: auto; border-radius: 8px; display: block;" width="200"/>
                                                <p style="font-size: 0.95em; color: #555555; margin: 5px 0 0 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Lucien Kael Marrow</p>
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
            <td class="section-padding" style="background-color: #f8f8f8; padding: 20px 20px;">
                <div class="level-up-container" style="background-color: #f0f0f0; padding: 15px; border-radius: 8px; text-align: center;">
                    <h2 style="font-size: 1.4em; font-weight: bold; color: #333333; margin-top: 0; margin-bottom: 18px; padding-bottom: 10px; border-bottom: 2px solid #dddddd; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.3;">Unlock Exclusive iBee Swag: Share the Knowledge, Reap the Rewards 🚀!</h2>
                    <p style="font-size: 0.95em; margin-bottom: 20px; color: #555555; margin-top: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">
                        Share the iBee Analytics newsletter and earn some fantastic free iBee swag!
                    </p>
                    <div style="text-align: center; margin-bottom: 25px;">
                        <img alt="Products" class="product-gif" height="220" src="https://ibeeanalytics.com/newsletter/product.gif" style="width: 300px; height: 310px; border-radius: 10px; display: inline-block;" width="250"/>
                    </div>
                    <table border="0" cellpadding="0" cellspacing="0" class="rewards-table" role="presentation" style="width: 100%; margin-top: 20px; border-collapse: separate; border-spacing: 0 8px;" width="100%">
                        <tr>
                            <td colspan="2" style="text-align: center; background-color: transparent; box-shadow: none; padding-bottom: 0; padding-top: 0; font-size: 1em; line-height: 1.5;">
                                <strong style="color: #007bff; font-size: 1.1em; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">🎉 Your Rewards Await! 🎉</strong>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">5 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Stickers</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">10 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Pen Stand</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">15 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Tote</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">25 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Coffee Mug</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">50 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Mystery Box</span>
                            </td>
                        </tr>
                        <tr>
                            <td style="text-align: left; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <strong style="color: #333333;">100 Referrals</strong>
                            </td>
                            <td style="text-align: right; background-color: #ffffff; padding: 12px 15px; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.07); vertical-align: middle; font-size: 0.95em; line-height: 1.5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <span style="color: #555555;">Work Table Setup</span>
                            </td>
                        </tr>
                    </table>
                    <p class="referral-info" style="font-size: 0.95em; margin-top: 25px; color: #555555; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Your referral count: <span style="font-weight: bold;">"""+recipient[2]+"""</span></p>
                    <div style="text-align: center; margin-top: 20px;">
                        <a class="cta-button" href="https://ibeeanalytics.com/newsletter.php?us="""+recipient[0]+"""' style="display: inline-block; padding: 12px 25px; background-color: #007bff; color: #ffffff !important; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 1em; letter-spacing: 0.5px; mso-hide: all; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Share Now &amp; Earn Rewards!</a>
                    </div>
                    <p class="referral-link-text" style="font-size: 0.85em; color: #777777; margin-top: 15px; display: block; word-break: break-all; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5;">Or copy &amp; paste your referral link: <a href="https://ibeeanalytics.com/newsletter.php?us="""+recipient[0]+"""' style="color: #777777; text-decoration: underline;">https://ibeeanalytics.com/newsletter.php?us="""+recipient[0]+"""</a></p>                </div>
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
# check url 
# count section 
# check subject 
# check page 