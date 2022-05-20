import os
import pandas as pd

def read_data_from_chosen_csv(full_path):

    if os.path.isfile(full_path):
        data = pd.read_csv(full_path, sep=',')
        df_name = pd.DataFrame(data, columns = ['Angle', 'Magnet current (A)', 'R2w', 'R2werr', 'Theta2w', 'R1w', 'R1werr', 'Theta1w', 'X2', 'Y2', 'X1', 'Y1', 'I_source (mA)', 'f_source (Hz)'])
        
    else:
        return print("File doesn't exist. Please use a directory or file that exists.")

    #Assign easy to use headers
    angle = df_name['Angle']
    magnet_current = df_name['Magnet current (A)'] 
    r2w = df_name['R2w']
    r2werr = df_name['R2werr']
    theta2w = df_name['Theta2w']
    r1w = df_name['R1w']
    r1werr = df_name['R1werr']
    theta1w = df_name['Theta1w']
    x2 = df_name['X2']
    y2 = df_name['Y2']
    x1 = df_name['X1']
    y1 = df_name['Y1']
    i_source = df_name['I_source (mA)']
    f_source = df_name['f_source (Hz)']

    array_of_data = [angle, magnet_current, r2w, r2werr, theta2w, r1w, r1werr, theta1w, x2, y2, x1, y1, i_source, f_source]
    
    return array_of_data


def plot_csv(data_frame, x_axis, y_axis):
    fig = px.line(data_frame, x = data_frame[x_axis], y = data_frame[y_axis], title= f'Graph of {array_of_names[x_axis]} vs {array_of_names[y_axis]}')
    
    fig.show()




#def alt_read_data_from_chosen_csv(full_path):
#
#    if os.path.isfile(full_path):
#        data = pd.read_csv(full_path)
#        df_name = pd.DataFrame(data, columns = ['Angle', 'Magnet current (A)', 'R2w', 'R2werr', 'Theta2w', 'R1w', 'R1werr', 'Theta1w', 'X2', 'Y2', 'X1', 'Y1', 'I_source (mA)', 'f_source (Hz)'])
#        df_name = df_name.values
#    else:
#        return print("File doesn't exist. Please use a directory or file that exists.")
    
#    return df_name