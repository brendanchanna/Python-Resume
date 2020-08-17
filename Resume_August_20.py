#Header text
Name = 'BRENDAN HANNA'
Subtitle = 'This resume was created using Python \n View the source code here: \n https://github.com/brendanchanna/Python-Resume.git'
Email = 'brendanchanna@gmail.com'
phone = '610-653-4031'
linkedin = 'www.linkedin.com/in/brendan-hanna'
#Skills section ------------------------------------------------------------------------------------------------------------------
SecHeader1 = 'SKILLS'
Skill1 = 'AWS'
Skill2 = 'Database Architecture'
Skill3 = 'Data Engineering'
Skill4 = 'Financial Modeling'
Skill5 = 'GitHub'
Skill6 = 'Hadoop'
Skill7 = 'Jupyter Notebook'
Skill8 = 'Microsoft Office'
Skill9 = 'Programming'
#Tech Expertise section
SecHeader2 = 'DATA EXPERTISE'
TE1 = 'Analysis | Python'
TEDesc1 = 'Cleaning | Mining | Modeling | Validation'
TE2 = 'Management | SQL'
TEDesc2 = 'Data Structure | Complex Query Development | Big Data Manipulation '
TE3 = 'Visualization | Tableau & Power BI'
TEDesc3 = 'Business Intelligence| Dashboard Design | KPI & Reporting'


#Experience section ------------------------------------------------------------------------------------------------------------------
SecHeader3 = 'EXPERIENCE'
#1
PLE1 = '\u25CF Data Engineer'
PLEloc1 = '-Addiction Solutions, State College, PA / May 2019 – May 2020'
PLEDesc1 =  '- Independently designed, built, tested, and implemented a new data structure and \n   schema to replace an existing file system for a rehabilitation clinic using SQL. \n - Provided operational support throughout the deployment of the system \n   while generating Tableau dashboards to help the client identify trends. '


#2
PLE2 = '\u25CF Data Analyst'
PLEloc2 = '- Life Cycle Assessment Consultation, State College, PA / Aug 2019 – Dec 2019'
PLEDesc2 = '- Functioned as the data analyst lead for a team conducting a cradle-to-grave life cycle \n   analysis of popular coffee pod materials to identify the most sustainable product \n   profile for a small business start-up. \n - Compiled results into a comprehensive Power BI report with recommendations \n   to improve environmental and fiscal sustainability for the client. '
#3
PLE3 = '\u25CF Director of Operations'
PLEloc3 = '- Penn State THON, State College, PA / April 2018– April 2019'
PLEDesc3 = '- Led the 777 Operations committee members in the logistical \n   planning and execution of all THON events while developing strategic sustainability, \n   zero waste, and environmental initiatives for the THON community. \n - Entrusted with the leadership of the world’s largest student-run philanthropy \n   as we worked tirelessly to raise over $10 million  for childhood cancer \n   treatment and research annually.'

#4
PLE4 = '\u25CF Director of Operations'
PLEloc4 = '- Penn State THON, State College, PA / April 2018 – Spring 2019'
PLEDesc4 = '- Led the 700+ members of the THON Operations Committee in the \n  logistical planning and execution of all THON events while developing strategic \n  sustainability, zero waste, and environmental initiatives for the THON community. \n - Acted as one of the 17 Directors of the world’s largest student-run philanthropy as we worked 60+ hours each week to raise over $10,000,000 for childhood cancer treatment and research in 2019. '

#5
PLE5 = '\u25CF Student Trainee'
PLEloc5 = '- United States Army Corps of Engineers, Philadelphia, PA / May 2018 – August 2018'
PLEDesc5 = '- Supported the Director of Operations in the maintenance and function of the \n  Fort Mifflin facilities and equipment through the regular use of power tools \n  and heavy machinery.'
#Education section ------------------------------------------------------------------------------------------------------------------
SecHeader4 = 'EDUCATION & \nACADEMIC ACHIEVEMENT'
EAA1 =  'Bachelor of Science'
EAA1Sub1 = 'Pennsylvania State University'
EAA1Sub2 = 'Spring 2016 - Spring 2020'
EAA2 = 'Dean\'s List'
EAA2Sub1 = 'Pennsylvania State University'
EAA2Sub2 = 'Fall 2019 | Spring 2020'
EAA3 = 'Skull & Bones \n Senior Honor Society'
EAA3Sub1 = 'Pennsylvania State University'
EAA3Sub2 = 'Member | Spring 2019'

#matplotlib plot style
import matplotlib.pyplot as plt
%matplotlib inline

#Constraints for the resume
fig, ax = plt.subplots(figsize=(9.75, 11))
ax.set_facecolor('white')
plt.axis('off')
plt.rcParams["font.family"] = "Calibri"
#Borders
plt.axvline(x=0, ymin=0, ymax=1, color='lightslategray', linewidth=.4)
plt.axvline(x=1, ymin=0, ymax=1, color='lightslategray', linewidth=.4)
plt.axhline(y=0, xmin=0, xmax=1, color='lightslategray', linewidth=.4)

#Dividing line parameters
plt.axvline(x=.3, ymin=.05, ymax=.75, color='steelblue', linewidth=1.5)
#topline
plt.axhline(y=.75, xmin=.10, xmax=.6, color='steelblue', linewidth=1.5)
#rightline
plt.axhline(y=.53, xmin=.3, xmax=.80, color='steelblue', linewidth=1.5)
#leftline
plt.axhline(y=.30, xmin=0, xmax=.3, color='steelblue', linewidth=1.5)
#topbox
plt.axhline(y=1, xmin=0, xmax=1, color='steelblue', linewidth=200)

#Format text
#Header section
plt.annotate(Name, (.02,.94), weight='bold', fontsize=25, color='white')
plt.annotate(Subtitle, (.99,.84), horizontalalignment='right', weight='regular', fontsize=11, color='white' )
plt.annotate(Email, (.02,.87), weight='heavy', fontsize=14, color='white')
plt.annotate(phone, (.02,.85), weight='heavy', fontsize=14, color='white')
plt.annotate(linkedin, (.02, .89), weight='heavy', fontsize=14, color='white')

#Skills section 
plt.annotate(SecHeader1, (.10,.76), weight='bold', fontsize=14, color='black')
plt.annotate(Skill1, (.28,.72), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill2, (.28,.68), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill3, (.28,.64), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill4, (.28,.60), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill5, (.28,.56), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill6, (.28,.52), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill7, (.28,.48), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill8, (.28,.44), horizontalalignment='right', weight='regular', fontsize=12)
plt.annotate(Skill9, (.28,.40), horizontalalignment='right', weight='regular', fontsize=12)

#Data Expertise section
plt.annotate(SecHeader2, (.6,.76), horizontalalignment='right', weight='bold', fontsize=14, color='black')
plt.annotate(TE1, (.33,.72), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc1, (.33,.70), weight='regular', fontsize=11, color='black')
plt.annotate(TE2, (.33,.66), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc2, (.33,.64), weight='regular', fontsize=11, color='black')
plt.annotate(TE3, (.33,.60), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc3, (.33,.58), weight='regular', fontsize=11, color='black')
#plt.annotate(TE4, (.33,.57), weight='bold', fontsize=12, color='black')
#plt.annotate(TEDesc4, (.33,.55), weight='regular', fontsize=11, color='black')

#Experience Section
plt.annotate(SecHeader3, (.33,.54), weight='bold', fontsize=14, color='black')
plt.annotate(PLE1, (.32,.5), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc1, (.34,.48), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc1, (.34,.41), weight='regular', fontsize=10, color='black')
plt.annotate(PLE2, (.32,.37), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc2, (.34,.35), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc2, (.34,.26), weight='regular', fontsize=10, color='black')
plt.annotate(PLE3, (.32,.22), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc3, (.34,.20), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc3, (.34,.09), weight='regular', fontsize=10, color='black')
#Additional annotation from previous versions
#plt.annotate(PLE4, (.32,.22), weight='bold', fontsize=12, color='black')
#plt.annotate(PLEloc4, (.34,.20), weight='light', fontsize=10, color='black')
#plt.annotate(PLEDesc4, (.34,.145), weight='regular', fontsize=10, color='black')
#plt.annotate(PLE5, (.32,.115), weight='bold', fontsize=12, color='black')
#plt.annotate(PLEloc5, (.34,.095), weight='light', fontsize=10, color='black')
#plt.annotate(PLEDesc5, (.34,.04), weight='regular', fontsize=10, color='black')

#Education section
plt.annotate(SecHeader4, (.01,.314), weight='bold', fontsize=14, color='black')
plt.annotate(EAA1, (.28,.27), horizontalalignment='right', weight='bold', fontsize=12, color='black')
plt.annotate(EAA1Sub1, (.28,.25), horizontalalignment='right', weight='regular', fontsize=10, color='black')
plt.annotate(EAA1Sub2, (.28,.23), horizontalalignment='right', weight='light', fontsize=10, color='black')
plt.annotate(EAA2, (.28,.19), horizontalalignment='right', weight='bold', fontsize=12, color='black')
plt.annotate(EAA2Sub1, (.28,.17), horizontalalignment='right', weight='regular', fontsize=10, color='black')
plt.annotate(EAA2Sub2, (.28,.15), horizontalalignment='right', weight='light', fontsize=10, color='black')
plt.annotate(EAA3, (.28,.09), horizontalalignment='right', weight='bold', fontsize=12, color='black')
plt.annotate(EAA3Sub1, (.28,.07), horizontalalignment='right', weight='regular', fontsize=10, color='black')
plt.annotate(EAA3Sub2, (.28,.05), horizontalalignment='right', weight='light', fontsize=10, color='black')

#save the plot/cut out white space
plt.subplots_adjust(wspace = 0)
plt.savefig('C:/PyPractice/B_Hanna_Python_Resume.png', dpi=300, bbox_inches='tight', pad_inches=0)
