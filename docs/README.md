# Salaire (Exploration de données)

## Description

Ce notebook a pour but d'explorer les données de salaire en 2023 au canada.
On veut aussi visualiser les données pour mieux comprendre les données.

### Resultat

<div id="maxSalary">
    The job that can has the max salary is:
      <span id="max">
        receptionist (bilingual) ontario simcoe county $ 713 000
      </span>
    <div>
      In the second place is: chief financial officer ontario greater toronto
      area $ 594 100
    </div>
    <div>The engineering jobs two most paid are:
      <ul>
        <li>engineering manager</li>
        <li>project engineer</li>
      </ul>
    </div>
    <div id="leastpayedregion">
      Get the engineers jobs that pay the least are in the following region:
      <ul>
        <li>windsor-essex county</li>
        <li>greater sudbury area</li>
        <li>brant county</li>
        <li>greater hamilton area</li>
      </ul>
    </div>
    <div id="minSalary">
      get the engineers jobs that pay the least
      <span id="min">
        structural engineering technologist ontario windsor-essex county $ 55
        000
      </span>
      In the second place is: chief financial officer ontario greater toronto
      area $ 594 100
    </div>
    <div id="quebecmostpayed">
      <table>
        <tr>
          <th>Province</th>
          <th>City</th>
          <th>Job Title</th>
          <th>Salary Range</th>
        </tr>
        <tr>
          <td>Quebec</td>
          <td>Montreal</td>
          <td>Chief Financial Officer</td>
          <td>$330,500 - $576,400+</td>
        </tr>
      </table>
    </div>
    <div>
      Quebec salary for cloud architect
      <table border="1" class="dataframe">
        <thead>
          <tr style="text-align: right">
            <th>job</th>
            <th>region</th>
            <th>mid_mean</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>cloud architect</td>
            <td>montréal</td>
            <td>127.65</td>
          </tr>
          <tr>
            <td>cloud architect</td>
            <td>laval</td>
            <td>125.80</td>
          </tr>
          <tr>
            <td>cloud architect</td>
            <td>saguenay-lac-saint-jean</td>
            <td>108.70</td>
          </tr>
          <tr>
            <td>cloud architect</td>
            <td>laurentides</td>
            <td>108.25</td>
          </tr>
          <tr>
            <td>cloud architect</td>
            <td>national capital</td>
            <td>108.25</td>
          </tr>
          <tr>
            <td>cloud architect</td>
            <td>estrie</td>
            <td>105.20</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="salary">
      <table>
        <tr>
          <th>job</th>
        </tr>
        <tr>
          <td>head of workshop and assembly</td>
          <td>206.50</td>
        </tr>
        <tr>
          <td>chief financial officer</td>
          <td>146.15</td>
        </tr>
        <tr>
          <td>controller</td>
          <td>97.00</td>
        </tr>
        <tr>
          <td>project coordinator</td>
          <td>90.90</td>
        </tr>
        <tr>
          <td>general manager</td>
          <td>85.35</td>
        </tr>
        <tr>
          <td>contracts administrator</td>
          <td>84.00</td>
        </tr>
        <tr>
          <td>vice president finance</td>
          <td>79.95</td>
        </tr>
        <tr>
          <td>data entry clerk</td>
          <td>74.00</td>
        </tr>
        <tr>
          <td>manufacturing director</td>
          <td>73.65</td>
        </tr>
        <tr>
          <td>inventory control manager</td>
          <td>70.65</td>
        </tr>
        <tr>
          <td>parts manager</td>
          <td>68.95</td>
        </tr>
        <tr>
          <td>program manager</td>
          <td>62.55</td>
        </tr>
        <tr>
          <td>director of operations</td>
          <td>59.60</td>
        </tr>
        <tr>
          <td>site supervisor</td>
          <td>58.60</td>
        </tr>
        <tr>
          <td>property manager</td>
          <td>52.55</td>
        </tr>
        <tr>
          <td>transportation manager</td>
          <td>51.80</td>
        </tr>
        <tr>
          <td>materials manager</td>
          <td>51.10</td>
        </tr>
        <tr>
          <td>director - financial planning &amp; analysis</td>
          <td>50.15</td>
        </tr>
        <tr>
          <td>finance director</td>
          <td>49.45</td>
        </tr>
        <tr>
          <td>qa/qc inspector</td>
          <td>48.95</td>
        </tr>
        <tr>
          <td>claims supervisor</td>
          <td>48.20</td>
        </tr>
        <tr>
          <td>office/operations manager</td>
          <td>47.55</td>
        </tr>
        <tr>
          <td>executive assistant</td>
          <td>45.95</td>
        </tr>
        <tr>
          <td>administrative manager</td>
          <td>44.20</td>
        </tr>
        <tr>
          <td>vice-president internal audit</td>
          <td>43.25</td>
        </tr>
        <tr>
          <td>health and safety manager</td>
          <td>42.55</td>
        </tr>
        <tr>
          <td>vice president human resources / chro</td>
          <td>
    </div>

    The job that pays the most is Dentistes with a maximum salary of 1076462.0
The job that pays the most in 2012 is Dentistes with a maximum salary of 1076462.0 in the Ontario
The job that pays the most in 2015 is Pharmaciens/pharmaciennes with a maximum salary of 923336.0 in the NB
The job that pays the most in 2013 is Médecins spécialistes with a maximum salary of 701878.0 in the Ontario
The job that pays the most in 2017 is Chiropraticiens/chiropraticiennes with a maximum salary of 667752.0 in the AB
The job that pays the most in 2016 is Chiropraticiens/chiropraticiennes with a maximum salary of 667752.0 in the Alberta
The job that pays the most in 2014 is Chiropraticiens/chiropraticiennes with a maximum salary of 667752.0 in the AB
The job that pays the most in 2020 is Médecins spécialistes with a maximum salary of 662709.6 in the MB
The job that pays the most in 2021 is Médecins spécialistes with a maximum salary of 662524.36 in the MB
The job that pays the most in 2019 is Médecins spécialistes with a maximum salary of 653910.18 in the MB
The job that pays the most in 2022 is Médecins spécialistes with a maximum salary of 637233.28 in the MB
The job that pays the most in 2018 is Avocats/avocates (partout au Canada) et notaires (au Quebec) with a maximum salary of 536822.0 in the AB
The job that pays the most is Ingénieurs/ingénieures d'industrie et de fabrication with a maximum salary of 684611.9999999999 in the province of Saskatchewan
The job that pays the most in Saskatchewan is Ingénieurs/ingénieures d'industrie et de fabrication with a maximum salary of 770188.5
The job that pays the most in Ontario is Ingénieurs géologues/ingénieures géologues with a maximum salary of 526500.0
The job that pays the most in AB is Ingénieurs miniers/ingénieures minières with a maximum salary of 507126.825
The job that pays the most in Alberta is Ingénieurs miniers/ingénieures minières with a maximum salary of 507126.05549999996
The job that pays the most in BC is Ingénieurs miniers/ingénieures minières with a maximum salary of 250229.24999999997
The job that pays the most in British Columbia is Ingénieurs miniers/ingénieures minières with a maximum salary of 249040.04850000003
The job that pays the most in Northwest Territories is Directeurs/directrices des services de génie with a maximum salary of 207582.75
The job that pays the most in ON is Inspecteurs/inspectrices d'ingénierie et officiers/officières de réglementation with a maximum salary of 194703.75
The job that pays the most in Newfoundland and Labrador is Ingénieurs/ingénieures de l'extraction et du raffinage du pétrole with a maximum salary of 186786.0
The job that pays the most in MB is Directeurs/directrices des services de génie with a maximum salary of 184983.75
The job that pays the most in NS is Directeurs/directrices des services de génie with a maximum salary of 180103.5
The job that pays the most in NL is Directeurs/directrices des services de génie with a maximum salary of 177187.5
The job that pays the most in NA is Directeurs/directrices des services de génie with a maximum salary of 175243.5
The job that pays the most in SK is Directeurs/directrices des services de genie with a maximum salary of 173076.75
The job that pays the most in Québec is Ingénieurs miniers/ingénieures minières with a maximum salary of 172532.70945
The job that pays the most in QC is Ingenieurs miniers/ingenieures minieres with a maximum salary of 172530.0
The job that pays the most in National is Ingénieurs/ingénieures de l'extraction et du raffinage du pétrole with a maximum salary of 170667.0
The job that pays the most in Nova Scotia is Ingénieurs/ingénieures de l'extraction et du raffinage du pétrole with a maximum salary of 166779.0
The job that pays the most in NB is Directeurs/directrices des services de génie with a maximum salary of 166475.25
The job that pays the most in CA is Ingénieurs/ingénieures de l'extraction et du raffinage du pétrole with a maximum salary of 165503.25000000003
The job that pays the most in PE is Directeurs/directrices des services de génie with a maximum salary of 161736.75
The job that pays the most in Manitoba is Directeurs/directrices des services de génie with a maximum salary of 161006.81445
The job that pays the most in New Brunswick is Ingénieurs informaticiens/ingénieures informaticiennes (sauf ingénieurs/ingénieures en logiciel) with a maximum salary of 154345.5
The job that pays the most in NT is Pilotes, navigateurs/navigatrices et instructeurs/instructrices de pilotage du transport aérien with a maximum salary of 146488.5
The job that pays the most in NW is Pilotes, navigateurs/navigatrices et instructeurs/instructrices de pilotage du transport aerien with a maximum salary of 146488.5
The job that pays the most in Quebec is Ingénieurs/ingénieures de l'extraction et du raffinage du pétrole with a maximum salary of 141304.5
The job that pays the most in Prince Edward Island is Ingénieurs civils/ingénieures civiles with a maximum salary of 110078.99999999999
The job that pays the most in Yukon Territory is Ingénieurs civils/ingénieures civiles with a maximum salary of 103335.75


