import smtplib
import time
from email.mime.text import MIMEText
# x denotes receiver mail id list
x=['libra688888@yahoo.com','ev.alban@gmail.com','pravinparmhar@gmail.com','asogan80@yahoo.com','yogeshsaravanakumar@gmail.com','eve.sandhya15@gmail.com','mshafat80@gmail.com','santhoshvnb@gmail.com','laminiyar@yahoo.com','mvangal@gmail.com','aras.thiru@gmail.com','vishalsarda444@gmail.com','yadavpratiksha14@gmail.com','vishal.singla87@yahoo.com','rudra_212004@yahoo.com','drmilindkumar@yahoo.com','harshvardhansraj@gmail.com','keshavf@yahoo.com','febinr@gmail.com','adiseshu72@gmail.com','padala2000@hotmail.com','hasilaa@gmail.com','xpgroover@hotmail.com','sriharimanojcbe@gmail.com','lini.karanath@gmail.com','tearintolife@gmail.com','senthsubra@gmail.com','vinmohfx@yahoo.com','uberalchemy@gmail.com','kabirdayal1988@gmail.com','h_s_zimmermann@arcor.de','neelnima@yahoo.com','shashivan@yahoo.com','nixson1971@hotmail.com','madegboyemikeadegb@gmail.com','kydissa@gmail.com','nvishy127@yahoo.com','siddhi.bharath@gmail.com','Kevingopaul007@yahoo.com','j_r_p_s@hotmail.com','hisupraja@gmail.com','msakthi.lak@gmail.com','sushma.db27@gmail.com','jinasraddha@gmail.com','Davidegili@yahoo.it','sanderannand@yahoo.com','sridevi_kk00@yahoo.com','Garudayogini@yahoo.com','rajesh4603@gmail.com','preety1509@gmail.com','sangarapillai@yahoo.com','rkshbhatt@gmail.com','mmsbt83@gmail.com','rbeasal@gmail.com','kalavala_79@hotmail.com','ananth.tvs@gmail.com','rajavenugopal31@yahoo.co.in','laxmivgj164@gmail.com','deechris27@gmail.com','robin.gentz@googlemail.com','eesincan@gmail.com','pradyukn@gmail.com','menonajay9@gmail.com','shivadas@msn.com','dushina20@yahoo.com','kymease@gmail.com','pearlbh@aol.com','sendswathi@yahoo.co.in','manos148@gmail.com','it.suriya@gmail.com','naintarakumari22@gmail.com','vaman.kpstore@googlemail.com','s.courreges.france@gmail.com','ktg.andr@gmail.com','sri@sribinajaya.com','nithi005@gmail.com','ssml0501@gmail.com','Amuda.ns@gmail.com','prasannakn84@yahoo.com','s.mohanmca86@gmail.com','mehala.chandran@gmail.com','muralipandalapalli@yahoo.com','kavi.winn@gmail.com','maribaby87@gmail.com','mari.karuppiah@gmail.com','sriravindra@yahoo.com','jerrymichaelbrooks@gmail.com','viswa81@gmail.com','madhusudan.ns@gmail.com','vince@universalbanking.com']
# y denotes receiver name list
y=['Archna','Elizabeth','pravin','kathir','saravanakumar','Sandhya','Mohsin','santhosh','Laxmikant ','Manju','aras','vishal','pratiksha','Vishal Singla','vikram ','Milind','Harsh','KESHAV','Febin','Adiseshu','padala surendra kumar','hasila','MELANIE','sriharimanoj','Lini','Dorisa','selva','Vinod','Henna','Kabir','Horst Silvio','sunita','Shashidhar','s.viswanathan','Michael','yamuna','Viswanath','Bharath','Ramraj','Jose Roman ','Supraja','Senthil','Sushma','Jinasraddha','Davide','Thanasewari','Sridevi','Linda','Rajesh','Preeti ','Moorthy Vigneswara','Rakesh','Kamatchi','Rahul','subramanyam','Ananth','Raja','Pushparaj','Deepak','Robin','Esin','Pradyumna','Ajay','Steven','Dooshina','Taylor','Debra','Swathi','Manogaran','Suriya','Naintara','Vamathevan','SYLVIE','Kranti','Sri tharan','mohan','Sakthi Ssml','Amuda','Pradyumna','Mohan','Mehala','Murali ','Kavi Tha','Mari','Marimuthu','Ravindra','Jerry Michael','Viswanathan','Madhusudan','Vincent']
for i in range (0,len(x)): # 
	title = y[i]
	msg_00content='<p><span style="font-size: 14pt;font-family: arial,helvetica,sans-serif; ">Namaste {title},<br /></p>'.format(title=title)
	msg_1content='<p style="text-align: center;"><span style="font-size: 24pt; color: #ff6600; font-family: arial black,sans-serif;"><strong>Hanuman Jayanthi 2017 Special&nbsp;</strong></span></p>'
	msg_2content='<p style="text-align: center;"><span style="font-size: 24pt; color: #000080; font-family: times new roman,times,serif;"><strong><span style="color: #000080;">Panchamukha Hanuman</span><span style="color: #000080;">&nbsp;Homam &amp; Power Rituals</span></strong></span><br /><span style="color: #800000;"><strong><span style="font-size: 14pt; font-family: book antiqua,palatino,serif;">Get Power To Fulfill All Your Wishes &amp; Keep Planetary Doshas Away</span></strong></span></p>'
	msg_3content='<p style="text-align: justify;"><span style="font-family: arial,helvetica,sans-serif; font-size: 12pt; color: #000000;">Lord Hanuman is said to be an incarnation of Lord Shiva. He has great strength, might and his devotion to Lord Ram is well known. He is also a great intellect and many believe that He still exists and readily appears to mitigate problems of his devotees. On Hanuman Jayanthi, the Lord&rsquo;s birthday, people worship this great figure of the grand epic Ramayana with supreme reverence and glory. He grants strength and power to overcome all types of difficulties in life. He conquers evil powers and spirits through miracle blessings.&nbsp;We at Vedicfolks are going to perform Homam for the great form Panchamukha Hanuman on Hanuman Jayanthi which is one of the powerful forms of Lord Hanuman with five faces. <span style="color: #000000; font-family: arial,helvetica,sans-serif; font-size: 16px; font-style: normal; font-weight: 400; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; background-color: #ffffff; display: inline; float: none;">Worshipin</span>g this form on his birthday helps destroy all your planetary doshas and fulfills all wishes of devotees .&nbsp;</span></p>'
	msg_000content='<img src="http://www.vedicfolks.com/serviceimg/banner/banner_1512648818.jpg" alt="Mountain View">'
	msg_4content='<p style="text-align: center;"><span style="color: #ff6600; font-family: times new roman,times,serif; font-size: 24pt;"><strong>Powerful Rituals for Hanuman Jayanthi 2017</strong></span></p>'
	msg_5content='<p style="text-align: center;"><span style="color: #003300;"><strong><span style="font-family: verdana,geneva,sans-serif;">Scheduled Live On <span class="aBn" tabindex="0" data-term="goog_584116726"><span class="aQJ">December 18, 2017 6 AM IST</span></span>&nbsp;</span></strong></span></p>'
	msg_6content='<p style="text-align: justify;"><span style="font-size: 12pt; font-family: verdana,geneva,sans-serif;"><span style="color: #000080;"><strong>Panchamukha Hanuman Homam</strong></span>&nbsp;-&nbsp;<span style="color: #000000; font-family: arial,helvetica,sans-serif;">It is a powerful homa that keeps away bad effects of Saturn and all other planets. It also protects against black magic &amp; evil spirits. And also fulfills all your desires.</span></span></p>'
	msg_7content='<p style="text-align: justify;"><strong><span style="font-family: verdana,geneva,sans-serif; font-size: 12pt; color: #800000;"><span style="color: #000080;">Sri Rama Puja</span>&nbsp;</span></strong>-&nbsp;&nbsp;<span style="font-family: arial,helvetica,sans-serif; font-size: 12pt;"><span style="color: #000000;">A puja to Lord Sri Rama, removes pitru dosha and other doshas related to planets. It also invites prosperity and success.</span> </span><br /> <br /><span style="font-family: verdana,geneva,sans-serif; font-size: 12pt;"><span style="color: #000080;"><strong>Mritasanjeevani Puja </strong></span><span style="color: #000000;">-</span><strong><span style="color: #800000;">&nbsp;</span></strong></span><span style="font-family: arial,helvetica,sans-serif; font-size: 12pt; color: #000000;">It is a miracle remedy for relief from chronic diseases and also grants blessings of longevity.</span><br /> <br /><strong><span style="font-family: verdana,geneva,sans-serif; font-size: 12pt; color: #800000;"><span style="color: #000080;">Kakallur Panchamukha Anjaneya Temple Puja</span>&nbsp;</span></strong>-<strong>&nbsp;</strong><span style="color: #000000; font-family: arial,helvetica,sans-serif; font-size: 16px; font-style: normal; font-weight: 400; text-align: justify; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; background-color: #ffffff; display: inline; float: none;">A puja in this temple provides five-fold blessings of Lord Hanuman like removing fear of enemies, confering victory, driving out evil energies and granting Mukthi</span><span style="font-family: arial,helvetica,sans-serif; font-size: 12pt; color: #000000;">. </span></p>'
	msg_8content='<p style="text-align: justify;"><br /> <em><span style="font-family: verdana,geneva,sans-serif; font-size: 12pt; color: #000080;"><strong>Energised Lord Hanuman Statue</strong></span></em>&nbsp;-&nbsp;<span style="color: #000000; font-size: 12pt; font-family: arial,helvetica,sans-serif;">A statue of this mighty god in your home brings luck and fortune. Keep it wherever you want &amp; all your difficult time will disappear like magic.</span><br /><br /><span style="font-size: 12pt; font-family: verdana,geneva,sans-serif;"><em><span style="color: #000080;"><strong>Energised Copper Bracelet</strong></span></em>&nbsp;</span>-&nbsp;<span style="font-size: 12pt; font-family: arial,helvetica,sans-serif; color: #000000;">The energised bracelet emits powerful vibrations to give you strength and courage in your daily activities.</span></p>'
	msg_9content='<p style="text-align: justify;"><em><span style="font-size: 12pt; font-family: verdana,geneva,sans-serif; color: #000080;"><strong>Energised Hanuman Yantra</strong></span></em>&nbsp;-<span style="color: #000000; font-size: 12pt;">&nbsp;It is a powerful tool to get the blessings of Lord Hanuman in a big way. It helps stump enemies, wards off planetary influences and has many other benefits. </span><br /><br /></p>'
	msg_11content='<p><span style="font-size: 18pt; color: #ff0000;"><strong>Join us!</strong></span> <span style="font-size: 12pt;"><strong>To&nbsp;Attain Divine Strength, Fortune &amp; Power on the special day of Hanuman Jayanthi&nbsp;</strong></span></p>'
	msg_13content='<p><a href="http://www.vedicfolks.com/life-time-management/karma-remedies/shared-homam/hanuman-jayanthi-puja.html" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://www.vedicfolks.com/life-time-management/karma-remedies/shared-homam/hanuman-jayanthi-puja.html&amp;source=gmail&amp;ust=1513426667594000&amp;usg=AFQjCNFJWZJdYxV3XuOMTLvWWpxRcYQQ7Q">http://www.vedicfolks.com/<wbr />life-time-management/karma-<wbr />remedies/shared-homam/hanuman-<wbr />jayanthi-puja.html</a></p><p>&nbsp;</p>'
	msg_14content='<div class="m_6488917842376954028ox-9f45f14676-ox-c88d6a65a9-ox-2a35598177-ox-e0a64aef69-ox-8444da6b27-io-ox-signature">'
	msg_15content='<p><span style="font-family: times new roman,times,serif; font-size: 14pt;">Thanks &amp; Regards,</span></p>'
	msg_16content='<p><span style="font-family: helvetica,arial,sans-serif; font-size: 12pt;">Sharmiladevi. A,</span><em> Customer Support +91 7338766066 &nbsp; &nbsp; &nbsp; &nbsp;</em></p>'
	msg=msg_00content+msg_1content+msg_2content+msg_3content+msg_000content+msg_4content+msg_5content+msg_6content+msg_7content+msg_8content+msg_9content+msg_11content+msg_13content+msg_14content+msg_15content+msg_16content # Cascading All lines
	message = MIMEText(msg, 'html')
	message['From'] = 'Vedicfolks<vedicfolks@gmail.com>'
	message['To'] = x[i]
	# Enter the subject below
	message['Subject'] ='Last Call : Get Power To Fulfill All Your Wishes & Keep Planetary Doshas Away on Hanuman Jayanthi 2017'
	msg_full = message.as_string()
	server = smtplib.SMTP('smtp.gmail.com:587') #setting up service provider name : port number
	server.starttls() #asking server to start
	server.login('gayathrikannan54@gmail.com','sairam31')#Sender Mail, Sender Mail Password
	server.sendmail('gayathrikannan54@gmail.com',        # Send Mail,Sender Mail,Receiver Mail
                ['gayathrikannan54@gmail.com',x[i]],
                msg_full)
	print(" \n Sent to ",i,y[i]) # Sent Log
	server.quit() #asking server to quit
	time.sleep(14) #sleeptime 