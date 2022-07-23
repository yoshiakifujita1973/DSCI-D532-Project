def pandas_test():
    import pandas as pd
    import mysql.connector
    
def visualize_sql():
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    from math import pi
    import datetime

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')

    c = cnx.cursor()

    c. execute('''SELECT tipi1 + tipi6 AS Extraversion, tipi2 + tipi7 AS Agreeableness, tipi3 + tipi8 AS Conscientiousness,
    tipi4 + tipi9 AS Emotional_Stability, tipi5+ tipi10 AS Openness_to_Experience FROM dass_tipi''')

    df = pd.DataFrame(c.fetchall())

    tipi_average = {
          'Extraversion': df[0].mean(),
          'Agreeableness': df[1].mean(),
          'Conscientiousness': df[2].mean(),
          'Emotional_Stability': df[3].mean(),
          'Openness_to_Experience': df[4].mean(),
    }

    cnx.close

    df_avf = pd.DataFrame([tipi_average])

    skills = list(df)
    num_skills = len(skills)

    angles = [i / float(num_skills) * 2 * pi for i in range(num_skills)]

    # Set up colors
    ORANGE = '#FD7120'
    BLUE = '#00BFFF'
    BLACK = '#000000'
    GRAY = '#999999'

    # Clear the plot to start with a blank canvas.
    plt.clf()

    #plt.figure(figsize=(9,6))
    plt.figure(dpi=100, figsize=(5,4))

    # Create subplots for each data series
    series_1 = plt.subplot(1, 1, 1, polar=True)
    #series_2 = plt.subplot(1, 1, 1, polar=True)

    # Draw one x-axis per variable and add labels
    plt.xticks(angles, ['Extraversion','Agreeableness','Conscientiousness','Emotional_Stability','Openness_to_Experience'], color=BLACK, size=12)

    # Draw the y-axis labels. To keep the graph uncluttered,
    # include lines and labels at only a few values.
    plt.yticks(
      [5, 8],
      ['5', '8'],
      color=BLACK,
      size=12
    )

    # Constrain y axis to range 0-100
    plt.ylim(5,10)

    series_1_values = df_avf.loc[0] \
                        .values \
                        .flatten() \
                        .tolist()
    #series_1_values += series_1_values[:1]



    # Plot the first series
    series_1.set_rlabel_position(0)
    series_1.plot(
      angles,
      series_1_values,
      color=BLACK,
      linestyle='solid',
      linewidth=1,
      alpha=0.1
    )
    series_1.fill(
      angles,
      series_1_values,
      color=BLACK,
      alpha=0.1
    )

    system_time = datetime.datetime.now()

    t = (system_time.strftime("%m%d%H%M%S"))

    fname = 'visualization' + t + '.jpg'

    filepath = './templates/static/' + fname

    plt.savefig(filepath)
        
    return fname
    
def peasonal_visualize_filter(gender, race, age_min, age_max, depression, anxiety, stress):
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    from math import pi
    import datetime
    
    # Set up colors
    ORANGE = '#FD7120'
    BLUE = '#00BFFF'
    BLACK = '#000000'
    GRAY = '#999999'

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')

    c = cnx.cursor()
       
    strSQL = 'SELECT tipi1 + tipi6 AS Extraversion, tipi2 + tipi7 AS Agreeableness, tipi3 + tipi8 AS Conscientiousness, '
    strSQL = strSQL + 'tipi4 + tipi9 AS Emotional_Stability, tipi5+ tipi10 AS Openness_to_Experience FROM dass_tipi'
        
    strJoin = ' INNER JOIN dass_Test'
    strJoin = strJoin + ' ON dass_tipi.test_id = dass_test.test_id'
    strJoin = strJoin + ' INNER JOIN test_taker'
    strJoin = strJoin + ' ON dass_test.taker_id = test_taker.taker_id'
                         
    strWhere = "Not setted"
    
    if gender == 'Male':
        strWhere = ' WHERE test_taker.gender = 1'
        
        draw_color = BLUE
        
    elif gender == 'Female':       
        strWhere = ' WHERE test_taker.gender = 2'
        
        draw_color = ORANGE
        
    else:
        draw_color = BLACK
        
    # filter by race
    
    race_value = '0'

    if race == "Asian": 
        race_value = '10'

    elif race == "Arab":    
        race_value = '20'

    elif race == "Black": 
        race_value = '30'

    elif race == "Indigenous Australian":    
        race_value = '40'        

    elif race == "Native American": 
        race_value = '50'

    elif race == "White":    
        race_value = '60'

    if int(race_value) > 0:
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.race = ' + race_value
        else:
            strWhere = strWhere + ' AND test_taker.race = ' + race_value

    # filter by age
    if age_min != "select":
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.age > ' + age_min
        else:
            strWhere = strWhere + ' AND test_taker.age > ' + age_min        
        
    if age_max != "select":
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.age < ' + age_max
        else:
            strWhere = strWhere + ' AND test_taker.age < ' + age_max
            

    if strWhere != 'Not setted':
        strSQL = strSQL + strJoin + strWhere
    
    c. execute(strSQL)

    df = pd.DataFrame(c.fetchall())

    tipi_average = {
          'Extraversion': df[0].mean(),
          'Agreeableness': df[1].mean(),
          'Conscientiousness': df[2].mean(),
          'Emotional_Stability': df[3].mean(),
          'Openness_to_Experience': df[4].mean(),
    }

    cnx.close

    df_avf = pd.DataFrame([tipi_average])

    skills = list(df)
    num_skills = len(skills)

    angles = [i / float(num_skills) * 2 * pi for i in range(num_skills)]

    # Clear the plot to start with a blank canvas.
    plt.clf()

    #plt.figure(figsize=(9,6))
    plt.figure(dpi=100, figsize=(5,4))

    # Create subplots for each data series
    series_1 = plt.subplot(1, 1, 1, polar=True)
    #series_2 = plt.subplot(1, 1, 1, polar=True)

    # Draw one x-axis per variable and add labels
    plt.xticks(angles, ['Extraversion','Agreeableness','Conscientiousness','Emotional_Stability','Openness_to_Experience'], color=BLACK, size=12)

    # Draw the y-axis labels. To keep the graph uncluttered,
    # include lines and labels at only a few values.
    plt.yticks(
      [5, 8],
      ['5', '8'],
      color=BLACK,
      size=12
    )

    # Constrain y axis to range 0-100
    plt.ylim(5,10)

    series_1_values = df_avf.loc[0] \
                        .values \
                        .flatten() \
                        .tolist()
    #series_1_values += series_1_values[:1]



    # Plot the first series
    series_1.set_rlabel_position(0)
    series_1.plot(
      angles,
      series_1_values,
      color=draw_color,
      linestyle='solid',
      linewidth=1,
      alpha=0.1
    )
    series_1.fill(
      angles,
      series_1_values,
      color=draw_color,
      alpha=0.1
    )
    
    system_time = datetime.datetime.now()

    t = (system_time.strftime("%m%d%H%M%S"))

    fname = 'visualization' + t + '.jpg'

    filepath = './templates/static/' + fname

    plt.savefig(filepath)
        
    return fname

def peasonal_visualize_male_female(race, age_min, age_max, depression, anxiety, stress):
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    from math import pi
    import datetime
    
    # Set up colors
    ORANGE = '#FD7120'
    BLUE = '#00BFFF'
    BLACK = '#000000'
    GRAY = '#999999'

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')

    c = cnx.cursor()
       
    strSQL = 'SELECT tipi1 + tipi6 AS Extraversion, tipi2 + tipi7 AS Agreeableness, tipi3 + tipi8 AS Conscientiousness, '
    strSQL = strSQL + 'tipi4 + tipi9 AS Emotional_Stability, tipi5+ tipi10 AS Openness_to_Experience FROM dass_tipi'
        
    strJoin = ' INNER JOIN dass_test'
    strJoin = strJoin + ' ON dass_tipi.test_id = dass_test.test_id'
    strJoin = strJoin + ' INNER JOIN test_taker'
    strJoin = strJoin + ' ON dass_test.taker_id = test_taker.taker_id'
                            
    strWhere_m = ' WHERE test_taker.gender = 1'       
       
    strWhere_f = ' WHERE test_taker.gender = 2'
    
    strWhere = 'Not setted'
        
    # filter by race
    
    race_value = '0'

    if race == "Asian": 
        race_value = '10'

    elif race == "Arab":    
        race_value = '20'

    elif race == "Black": 
        race_value = '30'

    elif race == "Indigenous Australian":    
        race_value = '40'        

    elif race == "Native American": 
        race_value = '50'

    elif race == "White":    
        race_value = '60'

    if int(race_value) > 0:

        strWhere = ' AND test_taker.race = ' + race_value

    # filter by age
    if age_min != "select":
        if strWhere == 'Not setted':
            strWhere = ' AND test_taker.age > ' + age_min
        else:
            strWhere = strWhere + ' AND test_taker.age > ' + age_min        
        
    if age_max != "select":
        if strWhere == 'Not setted':
            strWhere = ' AND test_taker.age < ' + age_max
        else:
            strWhere = strWhere + ' AND test_taker.age < ' + age_max
            
    # Get male data
    if strWhere != 'Not setted':
        strSQL_m = strSQL + strJoin + strWhere_m + strWhere
    else:
        strSQL_m = strSQL + strJoin + strWhere_m
    
    c. execute(strSQL_m)

    df = pd.DataFrame(c.fetchall())

    tipi_average_male = {
          'Extraversion': df[0].mean(),
          'Agreeableness': df[1].mean(),
          'Conscientiousness': df[2].mean(),
          'Emotional_Stability': df[3].mean(),
          'Openness_to_Experience': df[4].mean(),
    }
    
    # Get female data
    if strWhere != 'Not setted':
        strSQL_f = strSQL + strJoin + strWhere_f + strWhere
    else:
        strSQL_f = strSQL + strJoin + strWhere_f
    
    c. execute(strSQL_f)

    df = pd.DataFrame(c.fetchall())

    tipi_average_female = {
          'Extraversion': df[0].mean(),
          'Agreeableness': df[1].mean(),
          'Conscientiousness': df[2].mean(),
          'Emotional_Stability': df[3].mean(),
          'Openness_to_Experience': df[4].mean(),
    }

    cnx.close

    df_avf_gender = pd.DataFrame([tipi_average_male, tipi_average_female])

    skills = list(df)
    num_skills = len(skills)

    angles = [i / float(num_skills) * 2 * pi for i in range(num_skills)]

    # Clear the plot to start with a blank canvas.
    plt.clf()

    #plt.figure(figsize=(9,6))
    plt.figure(dpi=100, figsize=(5,4))

    # Create subplots for each data series
    series_1 = plt.subplot(1, 1, 1, polar=True)
    series_2 = plt.subplot(1, 1, 1, polar=True)

    # Draw one x-axis per variable and add labels
    plt.xticks(angles, ['Extraversion','Agreeableness','Conscientiousness','Emotional_Stability','Openness_to_Experience'], color=BLACK, size=12)

    # Draw the y-axis labels. To keep the graph uncluttered,
    # include lines and labels at only a few values.
    plt.yticks(
      [5, 8],
      ['5', '8'],
      color=BLACK,
      size=12
    )

    # Constrain y axis to range 0-100
    plt.ylim(5,10)
    
    series_1_values = df_avf_gender.loc[0] \
                        .values \
                        .flatten() \
                        .tolist()

    series_2_values = df_avf_gender.loc[1] \
                        .values \
                        .flatten() \
                        .tolist()

    # Plot the first series
    series_1.set_rlabel_position(0)
    series_1.plot(
      angles,
      series_1_values,
      color=BLUE,
      linestyle='solid',
      linewidth=1,
      alpha=0.1
    )
    series_1.fill(
      angles,
      series_1_values,
      color=BLUE,
      alpha=0.1
    )
    
    # Plot the second series
    series_2.set_rlabel_position(0)
    series_2.plot(
      angles,
      series_2_values,
      color=ORANGE,
      linestyle='solid',
      linewidth=1,
      alpha=0.1
    )
    series_2.fill(
      angles,
      series_2_values,
      color=ORANGE,
      alpha=0.1
    )
    
    system_time = datetime.datetime.now()

    t = (system_time.strftime("%m%d%H%M%S"))

    fname = 'visualization' + t + '.jpg'

    filepath = './templates/static/' + fname

    plt.savefig(filepath)
        
    return fname
    
def dass_visualize_sql(dass_type):
    
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import datetime

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')
    c = cnx.cursor()
    
    # Gather sum score from all participants
    
    if dass_type == "AD":
    
        strSQL = 'SELECT AnxietyTotal AS Anxiety,'
        strSQL = strSQL + 'DepressionTotal AS Depression FROM dass_anxiety '
        strSQL = strSQL + 'INNER JOIN dass_depression '
        strSQL = strSQL + 'ON dass_anxiety.test_id = dass_depression.test_id'
        
        xtitle = 'Anxiety'
        ytitle = 'Depression'
        
    elif dass_type == "AS":
        
        strSQL = 'SELECT AnxietyTotal AS Anxiety,'
        strSQL = strSQL + 'StressTotal AS Stress FROM dass_anxiety '
        strSQL = strSQL + 'INNER JOIN dass_stress '
        strSQL = strSQL + 'ON dass_anxiety.test_id = dass_stress.test_id'
        
        xtitle = 'Anxiety'
        ytitle = 'Stress'
        
    elif dass_type == "DS":
        
        strSQL = 'SELECT DepressionTotal AS Depression,'
        strSQL = strSQL + 'StressTotal AS Stress FROM dass_depression '
        strSQL = strSQL + 'INNER JOIN dass_stress '
        strSQL = strSQL + 'ON dass_depression.test_id = dass_stress.test_id'
        
        xtitle = 'Depression'
        ytitle = 'Stress'
    
    c. execute(strSQL)

    df = pd.DataFrame(c.fetchall())
    
    cnx.close
    
    # Visualize distribution of anxiety score and depression score

    fig = plt.figure(dpi=100, figsize=(5,4))

    gs = GridSpec(4, 4)

    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    fig.add_subplot(gs[0,0:3]).set_title(xtitle)
    fig.add_subplot(gs[1:4, 3]).set_title(ytitle)
    ax_hist_y = fig.add_subplot(gs[0,0:3])
    ax_hist_x = fig.add_subplot(gs[1:4, 3])

    ax_scatter.scatter(df[0], df[1], alpha=0.2, color='black')
    ax_hist_x.hist(df[0], bins=20, orientation = 'horizontal', alpha=0.5, color='black')
    ax_hist_y.hist(df[1], bins=20, orientation = 'vertical', alpha=0.5, color='black')
    
    system_time = datetime.datetime.now()

    t = (system_time.strftime("%m%d%H%M%S"))

    fname = 'visualization' + t + '.jpg'

    filepath = './templates/static/' + fname

    plt.savefig(filepath)
        
    return fname

def dass_visualize_sql_filter(dass_type, gender, race, age_min, age_max):
    
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import datetime
    
    # Set up colors
    ORANGE = '#FD7120'
    BLUE = '#00BFFF'
    BLACK = '#000000'
    GRAY = '#999999'

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')
    c = cnx.cursor()
    
    # Gather sum score from all participants
    
    if dass_type == "AD":
    
        strSQL = 'SELECT AnxietyTotal AS Anxiety,'
        strSQL = strSQL + 'DepressionTotal AS Depression FROM dass_anxiety '
        strSQL = strSQL + 'INNER JOIN dass_depression '
        strSQL = strSQL + 'ON dass_anxiety.test_id = dass_depression.test_id'
        
        strJoin = ' INNER JOIN dass_Test'
        strJoin = strJoin + ' ON dass_anxiety.Test_ID = dass_test.test_id'
        strJoin = strJoin + ' INNER JOIN test_taker'
        strJoin = strJoin + ' ON dass_test.taker_id = test_taker.taker_id'
        
        xtitle = 'Anxiety'
        ytitle = 'Depression'
        
    elif dass_type == "AS":
        
        strSQL = 'SELECT AnxietyTotal AS Anxiety,'
        strSQL = strSQL + 'StressTotal AS Stress FROM dass_anxiety '
        strSQL = strSQL + 'INNER JOIN dass_stress '
        strSQL = strSQL + 'ON dass_anxiety.test_id = dass_stress.test_id'
        
        strJoin = ' INNER JOIN dass_Test'
        strJoin = strJoin + ' ON dass_anxiety.Test_ID = dass_test.test_id'
        strJoin = strJoin + ' INNER JOIN test_taker'
        strJoin = strJoin + ' ON dass_test.taker_id = test_taker.taker_id'
        
        xtitle = 'Anxiety'
        ytitle = 'Stress'
        
    elif dass_type == "DS":
        
        strSQL = 'SELECT DepressionTotal AS Depression,'
        strSQL = strSQL + 'StressTotal AS Stress FROM dass_depression '
        strSQL = strSQL + 'INNER JOIN dass_stress '
        strSQL = strSQL + 'ON dass_depression.test_id = dass_stress.test_id'
        
        strJoin = ' INNER JOIN dass_Test'
        strJoin = strJoin + ' ON dass_depression.Test_ID = dass_test.test_id'
        strJoin = strJoin + ' INNER JOIN test_taker'
        strJoin = strJoin + ' ON dass_test.taker_id = test_taker.taker_id'
        
        xtitle = 'Depression'
        ytitle = 'Stress'
        
    strWhere = "Not setted"
    
    # filter by gender       
    if gender == "Male":
               
        strWhere = ' WHERE test_taker.gender = 1'

        draw_color = BLUE
        
    elif gender == "Female":
        
        strWhere = ' WHERE test_taker.gender = 2'
        
        draw_color = ORANGE
        
    else:
        draw_color = BLACK
        
    # filter by race
    
    race_value = '0'

    if race == "Asian": 
        race_value = '10'

    elif race == "Arab":    
        race_value = '20'

    elif race == "Black": 
        race_value = '30'

    elif race == "Indigenous Australian":    
        race_value = '40'        

    elif race == "Native American": 
        race_value = '50'

    elif race == "White":    
        race_value = '60'

    if int(race_value) > 0:
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.race = ' + race_value
        else:
            strWhere = strWhere + ' AND test_taker.race = ' + race_value
            
    # filter by age
    if age_min != "select":
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.age > ' + age_min
        else:
            strWhere = strWhere + ' AND test_taker.age > ' + age_min        
        
    if age_max != "select":
        if strWhere == 'Not setted':
            strWhere = ' WHERE test_taker.age < ' + age_max
        else:
            strWhere = strWhere + ' AND test_taker.age < ' + age_max
            
    if strWhere != 'Not setted':
        strSQL = strSQL + strJoin + strWhere
    
    c. execute(strSQL)
    
    df = pd.DataFrame(c.fetchall())
    
    cnx.close
    
    # Visualize distribution of anxiety score and depression score

    fig = plt.figure(dpi=100, figsize=(5,4))

    gs = GridSpec(4, 4)

    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    fig.add_subplot(gs[0,0:3]).set_title(xtitle)
    fig.add_subplot(gs[1:4, 3]).set_title(ytitle)
    ax_hist_y = fig.add_subplot(gs[0,0:3])
    ax_hist_x = fig.add_subplot(gs[1:4, 3])

    ax_scatter.scatter(df[0], df[1], alpha=0.2, color=draw_color)
    ax_hist_x.hist(df[0], bins=20, orientation = 'horizontal', alpha=0.5, color=draw_color)
    ax_hist_y.hist(df[1], bins=20, orientation = 'vertical', alpha=0.5, color=draw_color)

    system_time = datetime.datetime.now()

    t = (system_time.strftime("%m%d%H%M%S"))

    fname = 'visualization' + t + '.jpg'

    filepath = './templates/static/' + fname

    plt.savefig(filepath)
        
    return fname