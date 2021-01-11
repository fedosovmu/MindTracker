

class AppContent:
    image_placeholder_text = 'Картинка'

    license_agreement_screen = {
        'text': 'Для использования приложения вы должны принять пользовательское соглашение',
        'agree_button_text': 'Принимаю',
        'disagree_button_text': 'Не принимаю'
    }

    mood_assessment_screen = {
        'header_text': 'Как ваше настроение?',
        'mood_agree_button_text': 'Принимаю',
        'skip_button_text': 'Пропустить',
        'mood_assessor': {
            'secondary_label_mood_text': 'Настроение',
            'secondary_label_pull_text': 'Потяни',
            'mood_names': {
                '1': 'Ужасно',
                '2': 'Плохо',
                '3': 'Не очень',
                '4': 'Нормально',
                '5': 'Неплохо',
                '6': 'Всё отлично',
                '7': 'Восхитительное',
            },
            'paths_to_mood_spheres': {
                i: f'data/images/mood_spheres/{i}.png' for i in range(1, 8)
            },
            'default_mood': 4
        }
    }
