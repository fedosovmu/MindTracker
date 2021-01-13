from kivy.utils import get_color_from_hex as hex


class AppColors:
    design_colors = {
        'Black': hex('#000000'),
        'Dark': hex('#1A1C20'),
        'MiniDark': hex('#2C2C31'),
        'MainColors/Basic': hex('#FFFFFF'),
        'SilverWhite': hex('#F9EFF6'),
        'White': hex('#FFFFFF'),
        'MoodColors/1': hex('#674A7A'),
        'MoodColors/2': hex('#A43485'),
        'MoodColors/3': hex('#EC4B68'),
        'MoodColors/4': hex('#FF709B'),
        'MoodColors/5': hex('#6C8AF3'),
        'MoodColors/6': hex('#02C1B6'),
        'MoodColors/7': hex('#30BA00'),
        'Purple/MegaDark': hex('#191327'),
        'Purple/SuperDark': hex('#261E35'),
        'Purple/Dark': hex('#322A42'),
        'Purple/TextSecondary': hex('#876D8F'),
        'Purple/Light': hex('#D3B2CA'),
        'MainColors/CTA': hex('#674A7A'),
    }

    app_background_color = design_colors['Purple/Dark']

    image_placeholder_text_color = design_colors['SilverWhite']
    image_placeholder_background_color = design_colors['Purple/SuperDark']

    main_button_text_color = design_colors['MainColors/Basic']
    main_button_normal_state_background_color = design_colors['MainColors/CTA']
    main_button_pressed_state_background_color = design_colors['Purple/Light']

    text_button_normal_state_text_color = hex('ACA5BA')
    text_button_pressed_state_text_color = design_colors['SilverWhite']

    main_text_color = design_colors['SilverWhite']

    mood_colors = {
        '1': design_colors['MoodColors/1'],
        '2': design_colors['MoodColors/2'],
        '3': design_colors['MoodColors/3'],
        '4': design_colors['MoodColors/4'],
        '5': design_colors['MoodColors/5'],
        '6': design_colors['MoodColors/6'],
        '7': design_colors['MoodColors/7']
    }

    mood_assessor_background_color = design_colors['Purple/SuperDark']
    mood_assessor_secondary_text_color = design_colors['Purple/TextSecondary']

    mood_assessor_slider_cursor_colors = mood_colors.copy()
    mood_assessor_slider_cursor_colors['1'] = hex('1D142A')