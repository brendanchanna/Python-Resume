#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Header text
Name = 'BRENDAN HANNA'
Subtitle = 'This resume was created using Python - View the source code here:'
Email = 'brendanchanna@gmail.com'
phone = '610-653-4031'
#Skills section
SecHeader1 = 'SKILLS'
Skill1 = 'ArcGIS'
Skill2 = 'AutoCAD'
Skill3 = 'Electrical System Design'
Skill4 = 'Financial Modeling'
Skill5 = 'Life Cycle Assessment'
Skill6 = 'Linear Programming'
Skill7 = 'Microsoft Office Suite'
Skill8 = 'Network Modeling'
Skill9 = 'Project Management'
#Tech Expertise section
SecHeader2 = 'TECHNICAL EXPERTISE'
TE1 = '\u25CF Python'
TEDesc1 = 'Data analysis & cleaning | Machine learning | Scripting'
TE2 = '\u25CF SQL'
TEDesc2 = 'Database structure & management | Complex query development'
TE3 = '\u25CF Excel'
TEDesc3 = 'VBA & Macros | Pivot tables | Conditional formatting | Simulation'
TE4 = '\u25CF Tableau'
TEDesc4 = 'Data visualization | Model creation & validation'
#Experience section
SecHeader3 = 'PROFESSIONAL & LEADERSHIP EXPERIENCE'
PLE1 = '\u25CF Craftsman'
PLEloc1 = '- KallaKreations, State College, PA / May 2019 – May 2020'
PLEDesc1 =  '- Cut, designed, and finished custom furniture for Dr. Scott Camazine’s online shop'
PLE2 = '\u25CF Vice President'
PLEloc2 = '- Skull & Bones Senior Honor Society, State College, PA / Spring 2019 – Spring 2020'
PLEDesc2 = '- Engaged new, active, and alumni members in the pursuit of maintaining the \n  tradition and leadership of this society dedicated to honoring humble \n  and unselfish University leaders.'
PLE3 = '\u25CF Executive Committee, Member'
PLEloc3 = '- Penn State THON, State College, PA / Spring 2018– Spring 2019'
PLEDesc3 = '- Entrusted with the leadership of the world’s largest student-run philanthropy \n  as we worked tirelessly to raise over $10 million  for childhood cancer \n  treatment and research annually.'
PLE4 = '\u25CF Director of Operations'
PLEloc4 = '- Penn State THON, State College, PA / Spring 2018 – Spring 2019'
PLEDesc4 = '- Led the 700+ members of the THON Operations Committee in the \n  logistical planning and execution of all THON events while developing strategic \n  sustainability, zero waste, and environmental initiatives for the THON community.'
PLE5 = '\u25CF Student Trainee'
PLEloc5 = '- United States Army Corps of Engineers, Philadelphia, PA / May 2018 – August 2018'
PLEDesc5 = '- Supported the Director of Operations in the maintenance and function of the \n  Fort Mifflin facilities and equipment through the regular use of power tools \n  and heavy machinery.'
#Education section
SecHeader4 = 'EDUCATION & \nACADEMIC ACHIEVEMENT'
EAA1 =  'B.S. BioRenewable Systems'
EAA1Sub1 = 'Pennsylvania State University'
EAA1Sub2 = 'Spring 2016 - Spring 2020'
EAA2 = 'Dean\'s List'
EAA2Sub1 = 'Pennsylvania State University'
EAA2Sub2 = 'Fall 2019 | Spring 2020'
EAA3 = 'Sustainability Research \n Competition'
EAA3Sub1 = 'Pennsylvania State University'
EAA3Sub2 = '1st Place | Fall 2019'

#matplotlib plot style
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

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
plt.annotate(Subtitle, (.02,.84), weight='regular', fontsize=10, color='white' )
plt.annotate(Email, (.99,.88), horizontalalignment='right', weight='heavy', fontsize=14, color='white')
plt.annotate(phone, (.99,.85), horizontalalignment='right', weight='heavy', fontsize=14, color='white')

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

#Tech Expertise section
plt.annotate(SecHeader2, (.6,.76), horizontalalignment='right', weight='bold', fontsize=14, color='black')
plt.annotate(TE1, (.33,.72), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc1, (.42,.72), weight='regular', fontsize=11, color='black')
plt.annotate(TE2, (.33,.68), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc2, (.39,.68), weight='regular', fontsize=11, color='black')
plt.annotate(TE3, (.33,.64), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc3, (.40,.64), weight='regular', fontsize=11, color='black')
plt.annotate(TE4, (.33,.60), weight='bold', fontsize=12, color='black')
plt.annotate(TEDesc4, (.43,.60), weight='regular', fontsize=11, color='black')

#Experience Section
plt.annotate(SecHeader3, (.33,.54), weight='bold', fontsize=14, color='black')
plt.annotate(PLE1, (.32,.5), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc1, (.34,.48), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc1, (.34,.46), weight='regular', fontsize=10, color='black')
plt.annotate(PLE2, (.32,.43), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc2, (.34,.41), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc2, (.34,.355), weight='regular', fontsize=10, color='black')
plt.annotate(PLE3, (.32,.325), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc3, (.34,.305), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc3, (.34,.25), weight='regular', fontsize=10, color='black')
plt.annotate(PLE4, (.32,.22), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc4, (.34,.20), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc4, (.34,.145), weight='regular', fontsize=10, color='black')
plt.annotate(PLE5, (.32,.115), weight='bold', fontsize=12, color='black')
plt.annotate(PLEloc5, (.34,.095), weight='light', fontsize=10, color='black')
plt.annotate(PLEDesc5, (.34,.04), weight='regular', fontsize=10, color='black')

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

plt.savefig('C:/PyPractice/Hanna_Python_Resume.pdf', dpi=300)


# In[ ]:




