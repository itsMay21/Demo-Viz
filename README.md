# CS661-final-project: DEMOGRAPHIC VISUALIZATION
Aim-: The aim of the project is to provide an interactive platform for exploring and comparing key indicators across nations.

## Directory structure-:
1. assets folder-: Contains CSS files for our frontend part.
2. Data_files-: Folder containing all the data files which are used for visualization. Files are in csv format.
3. app.py-: Main implementation file of our app, which links all the pages to our app.
4. pages-: Folder containing various pages of our app.
    * home_page.py-: Home page of our app containing brief background of the project and the team.
    * page1.py-: World trend page, showing variation of factor across globe.
    * page2.py-: Factor relation page, to derive relationship between factors and gdp.
    * page3.py-: World Heatmap page, to observe distribution of factor across globe.
    * page4.py-: Sectoral distribution page, to get idea of contribution of various sectors towards economy of nation.
    * page6.py-: Income category page, to view which country lies in which category along with group wise comparison among them.
    * page8.py-: Parallel-Coordinate map, so as to get idea of relations among various factor and income category.
    * page9.py-: Comparison page, to compare various factor across various countries.
    * settings.py-: Settings page, so as to change various settings of our app which also include pre-processing modification.

## Instructions to use it:
1. First install all the requirements as mentioned in requirement.txt
2. Then come inside dash directory by using command: cd dash
3. Then launch the app by: python app.py
4. There in terminal comes a link for local host. ctrl+click or copy and paste in any browser to launch it.

## Instructions to upload data files:
1. To upload data-files, user can upload it directly in Data_files folder, or can upload via interface provided under setting page. Though it should be noted, uploading via setting involve conversion of name to "uploaded_"+filename.
2. Also make sure file should be in .csv format, else would not rendered, and if setting was used, app would not accept it and prompt an error with interactive message.
3. Format of file should also be matched, else interactive error message willl pop up, if uploaded via settings.