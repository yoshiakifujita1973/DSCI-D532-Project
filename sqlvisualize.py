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

    plt.figure(figsize=(12,8))

    # Create subplots for each data series
    series_1 = plt.subplot(1, 1, 1, polar=True)
    #series_2 = plt.subplot(1, 1, 1, polar=True)

    # Draw one x-axis per variable and add labels
    plt.xticks(angles, ['Extraversion','Agreeableness','Conscientiousness','Emotional_Stability','Openness_to_Experience'], color=BLACK, size=15)

    # Draw the y-axis labels. To keep the graph uncluttered,
    # include lines and labels at only a few values.
    plt.yticks(
      [5, 8],
      ['5', '8'],
      color=BLACK,
      size=15
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