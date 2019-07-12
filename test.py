import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
#tips = sns.load_dataset("tips")
#t = pd.read_csv('urban_population.csv')
#print(t.columns[0])
#for col in t.columns:
  #  print(col)

#style=input("enter style:")
#compare=input("Compare : ")
#compare_country=input("compare country :")
#chart=input("data set : ")
print("\t1.Population")
print("\t2.Health")
print("\t3.Education")
category=input("Data Category (Number) : ")
if(category=="1"):
    folder=("population/")
    print("\t1.Total Population")
    print("\t2.Population Density")
    print("\t3.Median Age")
    print("\t4.Total Urban Population")
    print("\t5.Urban Population from Total Population as Precentage")
    print("\t6.Urabn Population Growth Precentage")
        
    #chart="life_expectancy"
    chart_num=input("Enter Category(Number) :")
    if(chart_num=="1"):
        ylbl="Population"
        title="Total Population"
        chart=(folder+"population.csv")
    elif(chart_num=="2"):
        chart=(folder+"pop_density.csv")
        ylbl="Population Density per km"
        title="Population Density"
    elif(chart_num=="3"):
        chart=(folder+"pop_median_age.csv")
        ylbl="Median Age in Years"
        title="Median Age of Population"
    elif(chart_num=="4"):
        chart=(folder+"urban_population.csv")
        ylbl="Population"
        title="Total Urban Population"
    elif(chart_num=="5"):
        chart=(folder+"urban_pop_tot_precentage.csv")
        ylbl="Percentage"
        title="Urban Population Percentage"
    elif(chart_num=="6"):
        chart=(folder+"urban_pop_growth_precentage.csv")
        ylbl="Percentage"
        title="Urban Population Growth"

    t = pd.read_csv(chart)

    compare_status=input("Do you want to compare with another country(y/n) :")
    if(compare_status=="y"):
        print("Afghanistan    \t        Albania			Algeria     		Andorra  		Angola	")
        print("Antigua and Barbuda     Argentina     		Armenia     		Australia		Austria	")
        print("Azerbaijan		Bahamas			Bahrain			Bangladesh		Barbados")	
        print("Belarus			Belgium			Belize			Benin			Bhutan	")
        print("Bolivia			Bosnia and Herzegovina	Botswana		Brazil			Brunei	")
        print("Bulgaria	        Burkina			Faso			Burundi			Cambodia")	
        print("Cameroon		Canada			Cape Verde		Cent. African Republic	Chad	")
        print("Chile			China			Colombia		Comoros			Congo, Dem. Rep.	")
        print("Congo, Rep.		Costa Rica		Cote d'Ivoire		Croatia			Cuba	")
        print("Cyprus			Czech Republic		Denmark			Djibouti		Dominica")	
        print("Dominican Republic	Ecuador			Egypt			El Salvador		Equatorial Guinea")	
        print("Eritrea			Estonia			Ethiopia		Fiji			Finland	")
        print("France			Gabon			Gambia			Georgia			Germany	")
        print("Ghana			Greece			Grenada			Guatemala		Guinea	")
        print("Guinea-Bissau		Guyana			Haiti			Holy See		Honduras")	
        print("Hungary			Iceland			India			Indonesia		Iran	")
        print("Iraq			Ireland			Israel			Italy			Jamaica	")
        print("Japan			Jordan			Kazakhstan		Kenya			Kiribati")	
        print("Kuwait			Kyrgyz 			Republic		Lao			Latvia		Lebanon")	
        print("Lesotho			Liberia			Libya			Liechtenstein		Lithuania	")
        print("Luxembourg		Macedonia, FYR		Madagascar		Malawi			Malaysia	")
        print("Maldives		Mali			Malta			Marshall Islands	Mauritania	")
        print("Mauritius		Mexico			Micronesia, Fed. Sts.	Moldova			Monaco	")
        print("Mongolia		Montenegro		Morocco			Mozambique		Myanmar	")
        print("Namibia			Nauru			Nepal			Netherlands		New Zealand	Nicaragua")	
        print("Niger			Nigeria			North Korea		Norway			Oman	")
        print("Pakistan		Palau			Palestine		Panama			Papua New Guinea")	
        print("Paraguay		Peru			Philippines		Poland			Portugal	")
        print("Qatar			Romania			Russia			Rwanda			Samoa	")
        print("San Marino		Sao Tome and Principe	Saudi Arabia		Senegal			Serbia	")	
        print("Seychelles		Sierra Leone		Singapore		Slovak Republic		Slovenia")	
        print("Solomon Islands		Somalia			South Africa		South Korea		South Sudan")	
        print("Spain			Sri Lanka		St. Kitts and Nevis	St. Lucia		St. Vincent and the Grenadines")	
        print("Sudan			Suriname		Swaziland		Sweden			Switzerland	")
        print("Syria			Tajikistan		Tanzania		Thailand		Timor-Leste	")
        print("Togo			Tonga			Trinidad and Tobago	Tunisia	Turkey		Turkmenistan	")
        print("Tuvalu			Uganda			Ukraine			United Arab Emirates	United Kingdom	")
        print("United States		Uruguay			Uzbekistan		Vanuatu			Venezuela	")
        print("Vietnam			Yemen			Zambia			Zimbabwe")



        
        compare_country=input("Country to compare with :")
        


    style="line"

    if(style=="line"):
        ax = sns.lineplot("year", "Sri Lanka", data=t,palette="Blues_d",legend="brief",label="Sri Lanka")
        if(compare_status=="y"):
            ax = sns.lineplot("year", compare_country, data=t,legend="brief",label=compare_country)
        plt.title(title)
        plt.ylabel(ylbl)
        plt.legend()
        plt.show()


if(category=="2"):
    folder=("health/")
    print("\t1.Life Expectancy")
    print("\t2.Child Morality (0-5 yrs)")
    print("\t3.People living with HIV")

    chart_num=input("Enter Category(Number) :")
    if(chart_num=="1"):
        ylbl="Year of Life Expectancy"
        title="Life Expectancy"
        chart=(folder+"life_expectancy.csv")
        
    elif(chart_num=="2"):
        chart=(folder+"child_mor.csv")
        ylbl="Deaths per 1000 Live Births"
        title="Child Morality (0-5 yrs)"
        
    elif(chart_num=="3"):
        chart=(folder+"hiv.csv")
        ylbl="Population"
        title="People living with HIV"


    t = pd.read_csv(chart)

    compare_status=input("Do you want to compare with another country(y/n) :")
    if(compare_status=="y"):
        print("Afghanistan    \t        Albania			Algeria     		Andorra  		Angola	")
        print("Antigua and Barbuda     Argentina     		Armenia     		Australia		Austria	")
        print("Azerbaijan		Bahamas			Bahrain			Bangladesh		Barbados")	
        print("Belarus			Belgium			Belize			Benin			Bhutan	")
        print("Bolivia			Bosnia and Herzegovina	Botswana		Brazil			Brunei	")
        print("Bulgaria	        Burkina			Faso			Burundi			Cambodia")	
        print("Cameroon		Canada			Cape Verde		Cent. African Republic	Chad	")
        print("Chile			China			Colombia		Comoros			Congo, Dem. Rep.	")
        print("Congo, Rep.		Costa Rica		Cote d'Ivoire		Croatia			Cuba	")
        print("Cyprus			Czech Republic		Denmark			Djibouti		Dominica")	
        print("Dominican Republic	Ecuador			Egypt			El Salvador		Equatorial Guinea")	
        print("Eritrea			Estonia			Ethiopia		Fiji			Finland	")
        print("France			Gabon			Gambia			Georgia			Germany	")
        print("Ghana			Greece			Grenada			Guatemala		Guinea	")
        print("Guinea-Bissau		Guyana			Haiti			Holy See		Honduras")	
        print("Hungary			Iceland			India			Indonesia		Iran	")
        print("Iraq			Ireland			Israel			Italy			Jamaica	")
        print("Japan			Jordan			Kazakhstan		Kenya			Kiribati")	
        print("Kuwait			Kyrgyz 			Republic		Lao			Latvia		Lebanon")	
        print("Lesotho			Liberia			Libya			Liechtenstein		Lithuania	")
        print("Luxembourg		Macedonia, FYR		Madagascar		Malawi			Malaysia	")
        print("Maldives		Mali			Malta			Marshall Islands	Mauritania	")
        print("Mauritius		Mexico			Micronesia, Fed. Sts.	Moldova			Monaco	")
        print("Mongolia		Montenegro		Morocco			Mozambique		Myanmar	")
        print("Namibia			Nauru			Nepal			Netherlands		New Zealand	Nicaragua")	
        print("Niger			Nigeria			North Korea		Norway			Oman	")
        print("Pakistan		Palau			Palestine		Panama			Papua New Guinea")	
        print("Paraguay		Peru			Philippines		Poland			Portugal	")
        print("Qatar			Romania			Russia			Rwanda			Samoa	")
        print("San Marino		Sao Tome and Principe	Saudi Arabia		Senegal			Serbia	")	
        print("Seychelles		Sierra Leone		Singapore		Slovak Republic		Slovenia")	
        print("Solomon Islands		Somalia			South Africa		South Korea		South Sudan")	
        print("Spain			Sri Lanka		St. Kitts and Nevis	St. Lucia		St. Vincent and the Grenadines")	
        print("Sudan			Suriname		Swaziland		Sweden			Switzerland	")
        print("Syria			Tajikistan		Tanzania		Thailand		Timor-Leste	")
        print("Togo			Tonga			Trinidad and Tobago	Tunisia	Turkey		Turkmenistan	")
        print("Tuvalu			Uganda			Ukraine			United Arab Emirates	United Kingdom	")
        print("United States		Uruguay			Uzbekistan		Vanuatu			Venezuela	")
        print("Vietnam			Yemen			Zambia			Zimbabwe")
        compare_country=input("Country to compare with :")
        


    style="line"

    if(style=="line"):
        ax = sns.lineplot("year", "Sri Lanka", data=t,palette="Blues_d",legend="brief",label="SriLanka")
        if(compare_status=="y"):
            ax = sns.lineplot("year", compare_country, data=t,legend="brief",label=compare_country)
        plt.title(title)
        plt.ylabel(ylbl)
        plt.legend()
        plt.show()

if(category=="3"):
    folder=("education/")
    print("\t1.Literacy 15yrs+")

    chart_num=input("Enter Category(Number) :")
    if(chart_num=="1"):
        ylbl="Percentage"
        title="Literacy of people 15yrs+"
        chart=(folder+"literacy.csv")
        
    


    t = pd.read_csv(chart)

    compare_status=input("Do you want to compare with another country(y/n) :")
    if(compare_status=="y"):
        print("Afghanistan    \t        Albania			Algeria     		Andorra  		Angola	")
        print("Antigua and Barbuda     Argentina     		Armenia     		Australia		Austria	")
        print("Azerbaijan		Bahamas			Bahrain			Bangladesh		Barbados")	
        print("Belarus			Belgium			Belize			Benin			Bhutan	")
        print("Bolivia			Bosnia and Herzegovina	Botswana		Brazil			Brunei	")
        print("Bulgaria	        Burkina			Faso			Burundi			Cambodia")	
        print("Cameroon		Canada			Cape Verde		Cent. African Republic	Chad	")
        print("Chile			China			Colombia		Comoros			Congo, Dem. Rep.	")
        print("Congo, Rep.		Costa Rica		Cote d'Ivoire		Croatia			Cuba	")
        print("Cyprus			Czech Republic		Denmark			Djibouti		Dominica")	
        print("Dominican Republic	Ecuador			Egypt			El Salvador		Equatorial Guinea")	
        print("Eritrea			Estonia			Ethiopia		Fiji			Finland	")
        print("France			Gabon			Gambia			Georgia			Germany	")
        print("Ghana			Greece			Grenada			Guatemala		Guinea	")
        print("Guinea-Bissau		Guyana			Haiti			Holy See		Honduras")	
        print("Hungary			Iceland			India			Indonesia		Iran	")
        print("Iraq			Ireland			Israel			Italy			Jamaica	")
        print("Japan			Jordan			Kazakhstan		Kenya			Kiribati")	
        print("Kuwait			Kyrgyz 			Republic		Lao			Latvia		Lebanon")	
        print("Lesotho			Liberia			Libya			Liechtenstein		Lithuania	")
        print("Luxembourg		Macedonia, FYR		Madagascar		Malawi			Malaysia	")
        print("Maldives		Mali			Malta			Marshall Islands	Mauritania	")
        print("Mauritius		Mexico			Micronesia, Fed. Sts.	Moldova			Monaco	")
        print("Mongolia		Montenegro		Morocco			Mozambique		Myanmar	")
        print("Namibia			Nauru			Nepal			Netherlands		New Zealand	Nicaragua")	
        print("Niger			Nigeria			North Korea		Norway			Oman	")
        print("Pakistan		Palau			Palestine		Panama			Papua New Guinea")	
        print("Paraguay		Peru			Philippines		Poland			Portugal	")
        print("Qatar			Romania			Russia			Rwanda			Samoa	")
        print("San Marino		Sao Tome and Principe	Saudi Arabia		Senegal			Serbia	")	
        print("Seychelles		Sierra Leone		Singapore		Slovak Republic		Slovenia")	
        print("Solomon Islands		Somalia			South Africa		South Korea		South Sudan")	
        print("Spain			Sri Lanka		St. Kitts and Nevis	St. Lucia		St. Vincent and the Grenadines")	
        print("Sudan			Suriname		Swaziland		Sweden			Switzerland	")
        print("Syria			Tajikistan		Tanzania		Thailand		Timor-Leste	")
        print("Togo			Tonga			Trinidad and Tobago	Tunisia	Turkey		Turkmenistan	")
        print("Tuvalu			Uganda			Ukraine			United Arab Emirates	United Kingdom	")
        print("United States		Uruguay			Uzbekistan		Vanuatu			Venezuela	")
        print("Vietnam			Yemen			Zambia			Zimbabwe")
        compare_country=input("Country to compare with :")
        


    style="line"

    if(style=="line"):
        ax = sns.lineplot("year", "Sri Lanka", data=t,palette="Blues_d",legend="brief",label="SriLanka")
        if(compare_status=="y"):
            ax = sns.lineplot("year", compare_country, data=t,legend="brief",label=compare_country)
        plt.title(title)
        plt.ylabel(ylbl)
        plt.legend()
        plt.show()
        
