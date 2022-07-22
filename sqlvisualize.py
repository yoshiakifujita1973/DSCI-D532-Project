def pandas_test():
    import pandas as pd
    import mysql.connector
    
def visualize_sql():
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    from math import pi

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

    plt.savefig('./templates/static/visualization.jpg')
    
def peasonal_visualize_filter(gender, race, age_min, age_max, depression, anxiety, stress):
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    from math import pi

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

    plt.savefig('./templates/static/visualization.jpg')
    
    
def dass_visualize_sql(dass_type):
    
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec

    cnx = mysql.connector.connect(user='gen_viewer', password='1234',
                                      host='127.0.0.1',
                                      database='trouble_shoot')
    c = cnx.cursor()
    
    # Gather sum of anxiety score and depression score from all participants

    c. execute('''SELECT Q2A + Q4A + Q7A + Q9A + Q15A + Q19A + Q20A + Q23A + Q25A + Q28A + Q30A + Q36A + Q40A + Q41A AS Anxiety, 
            Q3A + Q5A + Q10A + Q13A + Q16A + Q17A + Q21A + Q24A + Q26A + Q31A + Q34A + Q37A + Q38A + Q42A AS Depression FROM dass_anxiety
            INNER JOIN dass_depression
            ON dass_anxiety.test_id = dass_depression.test_id''')

    df = pd.DataFrame(c.fetchall())
    
    cnx.close
    
    # Visualize distribution of anxiety score and depression score

    fig = plt.figure(dpi=100, figsize=(5,4))

    gs = GridSpec(4, 4)

    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    ax_hist_y = fig.add_subplot(gs[0,0:3])
    ax_hist_x = fig.add_subplot(gs[1:4, 3])

    ax_scatter.scatter(df[0], df[1], alpha=0.2, color='black')
    ax_hist_x.hist(df[0], bins=20, orientation = 'horizontal', alpha=0.5, color='black')
    ax_hist_y.hist(df[1], bins=20, orientation = 'vertical', alpha=0.5, color='black')

    plt.savefig('./templates/static/dass_visualization.jpg')
    
    return dass_type