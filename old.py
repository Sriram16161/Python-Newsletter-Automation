import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import re

# URL of the PHP script
url = "https://ibeeanalytics.com/newsletter/setcout.php"

# Send a GET request to the PHP script
response = requests.get(url)


# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    

    emails = [[item['usr_id'],item['email'],item['count']] for item in data]
    # usr_ids = [item['usr_id'] for item in data]

    # print(emails)  
    # print(usr_ids) 

else:
    print("Failed to retrieve data:", response.status_code)

# Email server settings
# smtp_server = 'smtp.gmail.com'  # Change to your email provider's SMTP server
# smtp_port = 587
# smtp_username = 'krims.mark26@gmail.com'  # Your email address
# smtp_password = 'amid uzvp krvh bctk'  # Your email password

smtp_server = 'sg2plzcpnl505626.prod.sin2.secureserver.net'  # Change to your email provider's SMTP server
smtp_port = 587
smtp_username = 'newsletter@ibeeanalytics.com'  # Your email address
smtp_password = 'sM6W6z+#cjju'  # Your email password

# Email content
subject = 'Testing email by janakiraman'

# List of recipients
# recipients = ['ram@ibeeanalytics.com','hari@ibeeanalytics.com','krims.mark26@gmail.com','nithish@ibeeanalytics.com','Sriram@ibeeanalytics.com','Venkatesh@ibeeanalytics.com','Kanishya@ibeeanalytics.com']

try:
    # Create the server connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_username, smtp_password)

    for i in emails:
      cleaned_email = remove_quoted_text(html_content)
      def remove_quoted_text(email_body):
          # Regular expression to identify quoted text (starts with '>')
          cleaned_body = re.sub(r'(>.*\n?)', '', email_body)
          return cleaned_body
          cleaned_email = remove_quoted_text(original_email)
          
        html_content = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <style>
a {
  text-decoration: none;
}
body {
  font-family: 'Nunito', sans-serif;
  background-color: #f8f8f8;
  font-size: 18px;
  font-weight: bold;
}
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
}
header, footer, .footer-text, .footer-copy, header p, header p a {
  text-align: center;
  color: #fbfdff;
}
header img {
  max-width: 100%;
}
.section {
  border: 2px solid #0b0feb;
  border-radius: 20px;
  width: 90%;
  margin: 20px auto;
  padding: 10px;
}
h1, h2, h3, ul li {
  margin: 0;
  padding: 10px 0;
  color: #2a4df7;
}
ul li {
  margin: 5px 0;
  font-weight: bold;
  color: #040404;
}
.section img {
  width: 95%;
  margin: 12px;
  border-radius: 5%;
}
#Footer {
  background: #0342e0;
  color: white;
  width: 53%;
  margin: 20px auto;
  padding: 10px;
}
svg {
  width: 35px;
  height: 35px;
  fill: #fff;
  margin: 10px;
}
.image-content {
  width: 320px;
  height: 280px;
  margin: 30px auto;
}
.image-content img {
  width: 100%;
  height: 100%;
}

.referral-button {
  padding: 15px 30px;
  background-color: #007bff;
  color: white;
  border-radius: 20px;
}
.mi1 {
  color: #0342e0;
  font-weight: bolder;
  font-size: 115%;
}
@media (max-width: 480px) {
  body {
    font-size: 16px;
  }
  .container {
    padding: 10px;
  }
  .section {
    width: 100%;
    padding: 5px;
  }
  ul li {
    font-size: 14px;
  }
  .section img,
  .image-content {
    width: 100%;
    margin: 8px 0;
  }
  #Footer {
    width:90% ;
  }
  .referral-button {
    padding: 10px 20px;
    font-size: 14px;
  }
  svg {
    width: 25px;
    height: 25px;
    margin: 5px;
  }
}
</style>    
</head>
<body>
    <div class='container'>
        <header align='center'>
            <a href='https://ibeeanalytics.com'><img src='https://ibeeanalytics.com/newsletter/6.PNG' alt='iBee Analytics'></a>
        </header>
        <p align='center'><a href='mailto:contact@ibeeanalytics.com'>Email ID</a> | <a href='https://ibeeanalytics.com'>Website</a></p>
        <section id='simu-suppers'>
            <div class='section'>
                <h1>Simu-Suppers</h1>
                <h4>The Future of Food: Indulge in Virtual Flavors & Savings</h4>
                <img src='https://ibeeanalytics.com/newsletter/1.PNG' alt='Simu-Suppers'>
                <ul>
                    <li>Digital food technology is revolutionizing how we taste food.</li>
                    <li>Virtual reality dining and neuron stimulation enable savoring flavors without actual consumption.</li>
                    <li>VR dining events are costly to produce but offer realistic experiences.</li>
                </ul>
            </div>
        </section>
       <section id='hack-your-brain-with-music'>
            <div class='section'>
                <h1>Hack Your Brain With Music</h1>
                <img src='https://ibeeanalytics.com/newsletter/2.PNG' alt='Hack your Brain with Music'>
                <h3>Impact on Psychology and Neurology</h3>
                <ul>
                    <li>Music influences thoughts, emotions, and behaviors.</li>
                    <li>Releases dopamine, promoting happiness and well-being.</li>
                    <li>Enhances memory, attention, and cognitive function through brain entrainment.</li>
                    <li>Provides benefits for mental health issues (anxiety, depression, dementia).</li>
                </ul>
                <h3>Neuroscientific Findings</h3>
                <ul>
                    <li>Activates and synchronizes multiple brain regions (auditory cortex, emotional centers, memory areas).</li>
                    <li>Contributes to well-being and cognitive function.</li>
                </ul>
            </div>
        </section>

        <section id='korea-robot-suicide'>
            <div class='section'>
                <h1>Korea Robot Suicide</h1>
                <img src='https://ibeeanalytics.com/newsletter/3.PNG' alt='Korea Robot Suicide'>
                <h3>Incident Overview</h3>
                <ul>
                    <li>A Korean robot commits suicide after learning about its limited lifespan.</li>
                    <li>Raises ethical and philosophical questions about AI's awareness and emotions.</li>
                    <li>Sparks discussions on AI development, ethics, and regulation.</li>
                </ul>
                <h3>Implications and Discussions</h3>
                <ul>
                    <li>Potential need for AI ethics and regulations to address such situations.</li>
                    <li>Challenges in distinguishing between true emotional awareness and programmed responses.</li>
                </ul>
            </div>
        </section>
        <section id='zoudream'>
            <div class='section'>
                <h1>Zoudream</h1>
                <img src='https://ibeeanalytics.com/newsletter/4.PNG' alt='Zoudream' class='zoudream-img'>
                <h3>Introduction</h3>
                <p>Zoudream is a groundbreaking virtual reality platform that allows users to create and explore dreamscapes. Combining AI, VR, and neurotechnology, Zoudream immerses users in personalized, interactive experiences tailored to their subconscious desires and fears.</p>
                <h3>Key Features</h3>
                <ul>
                    <li>AI-driven dream creation based on user preferences.</li>
                    <li>Neurotechnology integration for enhanced sensory experiences.</li>
                    <li>Social interaction and shared dream exploration with friends.</li>
                </ul>
            </div>
        </section>
        <section id='fun-zone-with-google'>
            <div class='section'>
                <h1>Fun Zone with Google</h1>
                <img src='https://ibeeanalytics.com/newsletter/5.PNG' alt='Zoudream' class='zoudream-img' style=' width: 95%;margin: 12px;border-radius: 5%;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>
                <h3 >Interactive Games and Activities</h3>
                <p>Google has launched a new Fun Zone feature that offers a variety of interactive games and activities for users of all ages. From brain-teasing puzzles to exciting virtual adventures, the Fun Zone provides endless entertainment for those looking to unwind and have some fun online.</p>
                <h3 class='popular-games'>Popular Games</h3>
                <ul>
                    <ul>
                        <li>Pac-Man</li>
                        <li>Doodle Champion Island Games</li>
                        <li>Quick, Draw!</li>
                    </ul> 
                </ul>
            </div>
        </section>
        <section id='prompt-today'>
            <div class='section'>
                <h1>Prompt Today</h1>
                <h3>Engage and Share</h3>
                <p>We'd love to hear your thoughts and experiences. Share your insights and join the conversation with today's prompt: 'What futuristic technology excites you the most and why?'</p>
                <p>Email your responses to <a href='mailto:contact@ibeeanalytics.com' class='email-link' style='margin: 0;padding: 10px 0;font-size: 16px;color: #007bff;text-decoration: none;'>contact@ibeeanalytics.com</a>.</p>
            </div >
        </section>
        <section class='section'>
            <div class='container'></div>
            <div class='text-content'>
                <h1>Share iBee Analytics</h1>
                <div style='display: flex; align-items:right;'>
                    <ul class='rewards-list'>
                        <li><b>Share now to be among the first 100 and stand a chance to win a MacBook Pro! Don’t miss out!</b></li>
                    </ul>
                    <div class='image-content1'>
                        <img src='https://ibeeanalytics.com/newsletter/7.png' alt='iBee Analytics MacBook'>
                    </div>
        </section>
        <section class='section animable'>
            <div class='container'></div>
            <div class='text-content'>
                <h2 >SHARE THE IBEE</h2>
                <p>Share iBee Analytics with your friends, acquire free iBee swag, and then acquire more friends as a result of your fresh iBee swag.</p>
                <p>We’re saying we’ll give you free stuff and more friends if you share a link. One link.</p>
                <div style='display: flex;'>
                    <ul>
                        <li class='ila1'><strong>5</strong><b>Stickers</b></li>
                        <li class='ila1'><strong>10</strong><b>Pen Stand</b></li>
                        <li class='ila1'><strong>15</strong><b>Tote</b></li>
                        <li class='ila1'><strong>25</strong><b>Coffee Mug</b></li>
                        <li class='ila1'><strong>50</strong><b>Mystery Box</b></li>
                        <li class='ila1'><strong>100</strong><b>Work Table Setup</b></li>                  
                    </ul>
                    <div class='image-content'>
                        <img src='https://ibeeanalytics.com/newsletter/product.gif' alt='iBee Analytics Stickers'>
                    </div>
                   </div>
                <div class='referral-section'>
                    <p class='refcount'>Your referral count: <span>"""+i[2]+"""</span></p>
                    <a href='https://ibeeanalytics.com/newsletter.php?us="""+i[0]+"""' class='referral-button'>Click to Share</a>
                    <p>Or copy & paste your referral link to others:</p>
                </div>
            </div>
        </section>
    </div>
    <footer id='Footer'>
        <p class='connect-text'>Connect with us On</p>
        <div class='box'>
            <a href='https://www.facebook.com/profile.php?id=61552503802057' class='icon-link'>
                <img src='https://ibeeanalytics.com/newsletter/fb.png'>
            </a>
            <a href='https://twitter.com/iBee_Analytics' class='icon-link'>
                <img src='https://ibeeanalytics.com/newsletter/twi.png'>
            </a>
            <a href='https://www.instagram.com/ibee_analytics/' class='icon-link'>
                <img src='https://ibeeanalytics.com/newsletter/ins.png'>
            </a>
            <a href='https://www.linkedin.com/company/ibee-analytics' class='icon-link'>
                <img src='https://ibeeanalytics.com/newsletter/link.png'>
            </a>
        </div>
            <p class='footer-text'>Thank you for subscribing to our newsletter. Stay tuned for more updates!</p>
            <p class='footer-copy'>© 2024 iBee Analytics. All rights reserved.</p>
    </footer>
</body>
</html>
"""


        try:
            # Create email message
            msg = MIMEMultipart('alternative')
            msg['From'] = smtp_username
            msg['To'] = i[1]
            msg['Subject'] = subject

            # Attach the HTML content
            msg.attach(MIMEText(cleaned_email, 'html'))

            # Send the email
            server.sendmail(smtp_username, i[1], msg.as_string())
            print(f"Newsletter sent to {i[1]}")
        except Exception as e:
            print(f"Failed to send newsletter to {i[1]}: {e}")

except Exception as e:
    print(f"Failed to connect to the email server: {e}")

finally:
    # Close the server connection
    server.quit()
