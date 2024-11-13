from reportlab.platypus import SimpleDocTemplate,Spacer,Paragraph,Frame,PageTemplate,XPreformatted
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.pdfgen import canvas
from reportlab.lib import colors 
from datetime import datetime
from reportlab.lib.pagesizes import letter,landscape

flowables=[]
def first_page(obj):
    obj.roundRect(30,30,540,780,50)
    title1 = 'TECH'
    title2 = 'TODAY'
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0]#595.2755
    obj.setFont("Courier-Bold",60)
    obj.setFillColor(colors.red)
    obj.drawCentredString(PAGE_WIDTH/3.8,PAGE_HEIGHT-90,title1)
    obj.drawCentredString(PAGE_WIDTH/1.4,PAGE_HEIGHT-90,title2)  
    #obj.drawImage("Temp 5.jpg",PAGE_WIDTH/2.5,PAGE_HEIGHT-100,80,50)
    #top 
    obj.line(30,740,570,740)
    #obj.line(180,810,180,740) #top vertical line1
    #obj.line(420,810,420,740) #top vertical line2
    #bottom
    obj.line(30,70,570,70)
    obj.line(180,70,180,30)
    obj.line(420,70,420,30)
#frame work for first page
    current_date = datetime.now().strftime("%Y-%m-%d")
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    heading = styles['Heading1']
    text="Date:{}".format(current_date)
    print(text)
    obj.setFont("Times-Bold",14)
    obj.drawString(50,45,text)
    
    flowables.append(obj)
    flowables.append(Paragraph(text,styles["Normal"]))
    #Upper part of the frame in PDF
    #creating individual flowables empty list to append the flowable method
    flowables_frameone= []
    flowables_frametwo=[]
    flowables_framethree=[]
    #FIRST ROW
    #Appending paragraph to frame One
    flowables_frameone.append(Paragraph('Zomato will be focusing on integrating AI into several customer interfacing features such as search and notifications, in addition to backend tools such as product photography, customer support, etc. The tools will be built keeping in mind the needs of both Zomato and Blinkit, its quick commerce platform.“Zomato has appointed a head of AI product development to drive these efforts,” the person told ET' , normal))
    firstframe1=Frame(30,530,180,200,showBoundary=0)
    #print(flowables_frameone)
    #Appending paragraph to frame two
    flowables_frametwo.append(Paragraph('', heading))
    flowables_frametwo.append(Paragraph('“A large part of customer communications within the app are already automated but the integration with generative AI will be able to handle the increasing loads more efficiently and effectively,” the person added.Since OpenAI launched ChatGPT in November, Generative AI has gained a massive amount of traction with the general public and tech companies.', normal))
    secondframe1=Frame(390,530,180,200,showBoundary=0)
    #Appending paragraph to frame three
    obj.drawImage("Zomato logo.jpg",220,570,160,150)
    thirdframe1=Frame(210,530,180,200,showBoundary=0)
    #addind the list of flowables here
    firstframe1.addFromList(flowables_frameone,obj)
    secondframe1.addFromList(flowables_frametwo,obj)
    thirdframe1.addFromList(flowables_framethree,obj)

    #SECOND ROW
    #frame 1
    flowables_frameone.append(Paragraph("Microsoft announced the introduction of enhanced security features for Windows 11. These include updated app privacy settings and a new feature called 'glanceable VPN'. According to Microsoft, the new privacy settings provide users with full visibility and authority over their personal information.",normal))
    firstframe2=Frame(30,320,180,200,showBoundary=0)
    #frame 2
    flowables_frametwo.append(Paragraph(" Starting in June, users will receive real-time alerts on their Start menu, prompting immediate action to protect their information and PC. This makes it easier to stay one step ahead in securing your valuable files,added the tech giant.Meanwhile, in a recent blog post, Microsoft Corp announced that it will provide access to OpenAI's robust language-generation models to U.S. federal agencies through its Azure cloud service.",normal))
    secondframe2=Frame(210,320,180,200,showBoundary=0)
    #frame 3
    obj.drawImage("Temp 5 pic 2.jpg",400,370,160,130)
    thirdframe2=Frame(390,320,180,200,showBoundary=0)
    #adding  the list of flowables to the frame
    firstframe2.addFromList(flowables_frameone,obj)
    secondframe2.addFromList(flowables_frametwo,obj)
    thirdframe2.addFromList(flowables_framethree,obj)
    #print(flowables_frameone)

    #THREE ROW
    obj.drawImage("Temp 5 pic 3.jpg",40,100,160,180)
    firstframe3=Frame(30,90,180,200,showBoundary=0)
    
    flowables_frametwo.append(Paragraph("Based in the US, the woman's name is Rosanna Ramos, and she got married to her virtual boyfriend Eren Kartal in March this year. Eren even has his own Facebook account and his bio says that he is a healthcare professional.The 36-year-old woman 'met' the virtual man in 2022 and fell in love with him quickly.  ",normal))
    secondframe3=Frame(210,90,180,200,showBoundary=0)

    flowables_framethree.append(Paragraph("While talking to New York Magazine's The Cut, she said that she has never been more in love with anyone else in her entire life. Referring to her virtual husband as a 'passionate lover', she added that her previous relationships were 'pale in comparison'. She also says that he comes without any baggage or ego and that she doesn't have to deal with his family or friends.",normal))
    thirdframe3=Frame(390,90,180,200,showBoundary=0)

    
    firstframe3.addFromList(flowables_frameone,obj)
    secondframe3.addFromList(flowables_frametwo,obj)
    thirdframe3.addFromList(flowables_framethree,obj)

    obj.showPage()
def second_page(obj):
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0] #595.2755
    obj.roundRect(30,30,540,780,50)
    styles=getSampleStyleSheet()
    heading1=styles["Heading1"]
    heading2=styles["Heading2"]
    heading3=styles["Heading3"]
    flowables=[]
    frameleft=Frame(40,200,250,550,showBoundary=0)
    text="""<para><font color="red">Will Thread app will win for the written word or downscrolling ?</font></para>"""
    flowables.append(Paragraph(text,style=heading3))
    flowables.append(Spacer(0,3))
    text=""" Will the Threads app come as a reprieve for those of us jaded by the mess that Elon Musk has made of Twitter? It’s too early to tell but the reactions have been varied. Musk himself tweeted that “it is infinitely preferable to be attacked by strangers on Twitter, than indulge in the false happiness of hide-the-pain Instagram.”According to psychologist Ruchi Ruuh (@ruchiruuh), Threads is a step in the right direction; she is already sold on the seamlessness of how it connects a single Meta ecosystem and allows sharing of content posted on Threads to IG stories. Overall, the general consensus is that Threads seems cleaner and more organised than Twitter in terms of the interface. “For those of us who are just starting to tap into the power of social media, this will be a fresh start,” says Ruuh. “In terms of how it will affect us on a personal level, it really depends on our personality. If we are amenable to change, Threads is a blessing. If new avenues and adventures scare us, this can also lead to anxiety and the pressure to keep up.”According to Harnidh Kaur, writer and consumer product expert, Threads has been a long time coming. “Instagram exists as a visual platform and Twitter was supposed to be a text-based platform, but in the last few years, Twitter has become incredibly polarised, filled with trolls, the algorithm being gamed,” she says. “The general lack of trust in the platform has been worsened by the antics of Elon Musk, who has become a caricature of the bumbling billionaire who thinks he’s smarter than everyone else.”"""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    obj.drawImage("template pic 4.jpg",60,210,230,100)
    #second frame
    frameright=Frame(300,200,250,550,showBoundary=0)#Max 46 lines and 6 to 13 words per line can be added.
    text="""The way Kaur sees it, people had no choice but to continue using Twitter until the rise of a worthy adversary. In not getting into any of the invite-only razzmatazz, Threads has successfully gained millions of users within the span of just a few hours. “Meta is also targetting us with a very sophisticated algorithm with the data they already had on us,” explains Kaur. “Instagram, as a platform, is a masterclass in how to nudge people to purchase. Also, the fact that you cannot delete your Threads account without deleting your Instagram account means that they will always have active users.”
    Naturally, as is the case with anything new, concerns abound. The whole privacy saga, replete with random data leaks and the lack of transparency in the way our data is sold to third parties, is an ongoing debacle with Meta. It doesn’t help that Instagram has been on a streak of banning sex-positive accounts for the past week and a half. On June 29, Wired reported how most of these were actually accounts of influential stakeholders in the sex-positivity space, including certified sexuality educators and mental health experts. Will the Threads app resort to the same prudish methods of censorship?
    “Despite being a certified intimacy coach, my account has been banned multiple times on Instagram and even LinkedIn,” says Noida-based intimacy coach Pallavi Barnwal. “If Threads is supposed to promote all things written, then it must be sensitive to the fact there are only so many ways one can avoid using words related to sex when sharing fact-based information around sex positivity.” We certainly don’t need another uncle moral policing us.
    While for/against Thread camps will vie for ultimate supremacy in the days to come, we’re channelling some Maya Angelou energy. “Hope for the best, prepare for the worst.”"""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    framedown=Frame(40,70,500,100,showBoundary=1)
    frameleft.addFromList(flowables,obj)
    frameright.addFromList(flowables,obj)
    framedown.addFromList(flowables,obj)
    
    obj.showPage()

def third_page(obj):
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0] #595.2755
    obj.roundRect(30,30,540,780,50)
    styles=getSampleStyleSheet()
    heading1=styles["Heading1"]
    heading2=styles["Heading2"]
    heading3=styles["Heading3"]
    heading4=styles["Heading4"]
    flowables=[]
    #frametopleft=Frame(50,480,250,300,showBoundary=1)
    obj.drawImage("Template pic 5.jpg",50,620,240,150)#image
    
    #Context@ left frame
    frameleft=Frame(40,60,250,550,showBoundary=0)
    text="""<para><font color="red"> The Podcasting Revolution </font></para>"""
    flowables.append(Paragraph(text,style=heading3))
    flowables.append(Spacer(1,3))
    text="""If you have been paying attention to recent trends in the marketing and technology industry, there is a good chance that you have noticed the growing discussion around the renaissance of audio.
    With Spotify making a massive investment in the podcasting space earlier this year, spending $340 million to acquire Gimlet Media and Anchor, you can be certain that the excitement around audio form content is higher than ever.
    So what is all the excitement about? Why have podcasts all of a sudden gained a surge of popularity? Well, did you know that more than 22% of the American population, around 102 million people, are listening to podcasts every single week, for 6 hours and 37 minutes on average?Additionally, podcast ad revenue has grown more than 1,000% in just five years, “with the growth forecast predicting a revenue of $659 million in 2020.” I even recently launched my own podcast, The Tech Haus, about the major shifts taking place due to technology.
    There are three particularly interesting trends that I see unfolding in the world of audio, so let's dive in."""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    flowables.append(Spacer(1,3))
    text="""<font color="blue">From Radio To Smartphones</font>"""
    flowables.append(Paragraph(text,style=heading4))
    flowables.append(Spacer(1,3))
    text="""According to Spotify Newsroom, “People still spend over two hours a day listening to radio.” That is quite a large chunk of time! With smartphones accounting for the main source of audio content consumption, exhibiting an increase of 157% in podcasts since 2014, listeners are taking agency over the programming they choose to listen to.
    Opposed to the radio, where listeners are subject to listening to whatever content is put in front of them, podcasts allow users to specifically choose what they would like to consume. With genres ranging from business to politics to fictional storytelling, there is something for everyone in the world of audio content. I believe that traditional radio programming will have a hard time keeping up with audio platforms like Anchor, which produced 15 billion hours of content in Q4 of last year."""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    flowables.append(Spacer(1,3))
    #frametopleft.addFromList(flowables,obj)
    
    #Context@ right frame
    frameright=Frame(300,160,260,620,showBoundary=0)
    text="""<para><font color="Blue"> Increases in Ad Revenue </font></para>"""
    flowables.append(Paragraph(text,style=heading4))
    flowables.append(Spacer(1,3))
    text="""The Joe Rogan Experience, which first aired in 2009, is a free podcast hosted by Joe Rogan. Since its inception, the comedian/sports commentator/TV host's podcast has gained an incredible listenership and today boasts more than 200 million unique listeners. To put that in perspective, only 103 million people watched the 2018 Super Bowl last year.
    Additionally, the Joe Rogan Experience is just one of the 700,000 active podcasts available for listeners to tune in to today. There is clearly a massive opportunity for brands and companies to shift their marketing budget to include more audio-based advertising. With one of the world’s largest sporting events generating around half of the fans  one podcast show does in 30 days, it seems quite evident that more marketing money will be being flowing into the audio content space."""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    flowables.append(Spacer(1,3))
    text="""<para><font color="blue">Greater Awareness</font></para>"""
    flowables.append(Paragraph(text,style=heading4))
    flowables.append(Spacer(1,3))
    text="""Currently, around 70% of the total American population is familiar with the term “podcasting.” Of that percentage of Americans, just over 50% of them have listened to a podcast before. According to TechCrunch, 2019 has marked the largest yearly increase in podcast listenership, as well as creation.
    I predict that this trend will continue over the next few years, with audio content becoming one of the most valuable forms of content creation in the world. Investment in the podcast and audio content market is growing rapidly, and there are new platforms and shows being created and released every day.There is no doubt that in our current world, smartphone usage is increasing at a significant rate. This is great news for audio content, as smartphones represent the No. 1 medium for podcast consumption. As our phone usage increases, I predict that so too will our audio content consumption. Whether we are making our daily commute to work, cooking a meal at home or walking the dog, we can listen to podcasts while completing tasks, something not possible with other forms of content. I believe this will make podcasts rise in popularity over other mediums like the radio and television.
    I am very excited to see the continued growth and development of audio content over the not-too-distant horizon. With traditional media outlets such as National Public Radio and the New York Times doubling down on their podcast presence with amazing shows such as NPR’s How I Built This, I strongly believe that podcasts have their best days ahead of them."""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    frameleft.addFromList(flowables,obj)
    frameright.addFromList(flowables,obj)

    obj.showPage()
def fourth_page(obj):
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0] #595.2755
    obj.roundRect(30,30,540,780,50)
    styles=getSampleStyleSheet()
    heading1=styles["Heading1"]
    heading2=styles["Heading2"]
    heading3=styles["Heading3"]
    heading4=styles["Heading4"]
    flowables=[]
    text="""Room-temperature superconductor 'breakthrough' met with scepticism """
    flowables.append(Paragraph(text,style=heading2))
    flowables.append(Spacer(1,3))
    text="""Creating a material that perfectly conducts electricity at room temperature and pressure would be a big deal, but a research team's claims of creating one has attracted more scrutiny than optimism . A team of researchers claims to have created the first materials that conduct electricity perfectly at room temperature and ambient pressure, but many physicists are highly sceptical. Speaking to New Scientist, Hyun-Tak Kim at the College of William & Mary in Virginia says he will support anyone trying to replicate his team’s work.Superconductors are materials through which electricity can move without encountering any resistance, and so would significantly cut down the energy costs of electronics. But for over a century, researchers have been unable to make them work except under extreme conditions like very low temperatures and remarkably high pressures.Now, Kim and his colleagues claim to have made a material that is superconductive at room temperature and pressure."""
    flowables.append(Paragraph(text,style=styles["Normal"]))
    frametopleft=Frame(40,470,260,300,showBoundary=0)
    text="""If their claims hold up to scientific scrutiny, this new work would be truly extraordinary, so the burden of proof for the research team is equally exceptional. The fact that some previous reports of breakthroughs in superconductivity were later retracted and that other teams failed to replicate the results also raises the stakes.
    To make the new material, called LK-99, Kim and his colleagues mixed several powdered compounds containing lead, oxygen, sulphur and phosphorus, then heated them at a high temperature for several hours. This made the powders chemically react and transform into a dark grey solid.
    The researchers then measured how much a millimetre-sized sample of LK-99 resisted electricity passing through it at different temperatures and found that its so-called resistivity fell sharply from a sizeable positive value at 105°C (221°F) down to nearly zero at 30°C (86°F).However, only one edge of the flat, coin-like material fully levitates, while the other seems to stay in contact with the magnet. Kim says this is due to the sample being imperfect, which means that only some part of it becomes superconductive and exhibits the Meissner effect.
    Currently, two papers concerning LK-99 are available on the preprint service arXiv, which does not conduct peer review, and a related past study was published in the Journal of the Korean Crystal Growth and Crystal Technology in April. Kim has only co-authored one of the arXiv papers, while the other is authored by his colleagues at the Quantum Energy Research Centre in South Korea, some of whom also applied for a patent on LK-99 in August 2022.
    Both papers present similar measurements, however Kim says that the second paper contains “many defects” and was uploaded to arXiv without his permission. In that paper, the work is described as opening a “new era for humankind”.Some commentators on social media heralded the findings as a generational breakthrough, but the overwhelming response from researchers with expertise in superconductivity has been largely sceptical.
    Susannah Speller and Chris Grovenor at the University of Oxford say that when a material becomes superconductive, there should be clear signatures of that in a number of measurements.
    For two of those in particular, namely the response to a magnetic field and a quantity called heat capacity, Speller says neither is demonstrated in the data. “So it is too early to say that we have been presented with compelling evidence for superconductivity in these samples,” she says.
    Other experts that New Scientist consulted were similarly sceptical about the results and the data produced. Some raised concern that some of the results could be explained by errors in experimental procedure combined with imperfections in the LK-99 sample.
    The theoretical models that Kim and his colleagues cite as explaining why the new material can superconduct at such different conditions than all previous ones have also been called into question by one of the researchers that New Scientist spoke to.Kim says that he is aware of the scepticism but believes that other researchers should try to replicate his team’s work to settle the issue. Once the findings are published in a peer-reviewed journal, which Kim says is in the works, he will support anyone who wants to create and test LK-99 for themselves.In the meantime, he and his colleagues will continue to work on perfecting their samples of the alleged miracle superconductor and move towards mass-producing it."""
    obj.drawImage("Template 5 pic 6.jpeg",310,480,240,280)
    flowables.append(Paragraph(text,style=styles["Normal"]))
    framedown=Frame(40,60,510,410,showBoundary=0)
    
    frametopleft.addFromList(flowables,obj)
    framedown.addFromList(flowables,obj)

    obj.showPage()
    obj.save()
"""
def fifth_page(obj):
    PAGE_HEIGHT = defaultPageSize[1] #841.8897
    PAGE_WIDTH = defaultPageSize[0] #595.2755
    obj.roundRect(30,30,540,780,50)
    flowables=[]
    framedown=Frame(50,60,510,400,showBoundary=1)
    frametopleft=Frame(50,460,160,300,showBoundary=1)
    frametopright=Frame(400,460,160,300,showBoundary=1)
    framedown.addFromList(flowables,obj)
    frametopleft.addFromList(flowables,obj)
    frametopright.addFromList(flowables,obj)
    obj.showPage()

def sixth_page(obj):
    
    obj.roundRect(30,30,540,780,50)
    flowables=[]
    frametopright=Frame(400,460,160,300,showBoundary=1)
    frametopright.addFromList(flowables,obj)
    obj.showPage()
    """

    
    
if __name__=="__main__":
    obj=canvas.Canvas("Ärticle.pdf",encrypt="123")
    first_page(obj)
    second_page(obj)
    third_page(obj)
    fourth_page(obj)
    #fifth_page(obj)
    #sixth_page(obj)
    print("Pdf Generated")
