BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

STATE_CHOICES = [
('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]


LANGUAGE_COUNT_CHOICES = [
    ('1-2', '1 - 2 languages'),
    ('3-4', '3 - 4 languages'),
    ('4+', 'More than 4 languages'),
]

EXPERIENCE_CHOICES = [
    ('none', 'None'),
    ('less_than_a_year', 'Less than a year'),
    ('1-3', '1-3 years'),
    ('3-5', '3-5 years'),
    ('5+', 'More than 5 years'),
]

INTERPRETATION_STRENGTH_CHOICES = [
    ('none', 'I don\'t necessarily have a strength'),
    ('on_site', 'On-Site interpretation'),
    ('over_phone', 'Over-The-Phone interpretation'),
    ('escort', 'Escort interpretation'),
    ('consecutive', 'Consecutive interpretation'),
    ('simultaneous', 'Simultaneous interpretation'),
]

INTERPRETATION_FIELD_CHOICES = [
    ('none', 'I don\'t have any'),
    ('medical', 'Medical'),
    ('schools', 'Schools'),
    ('legal', 'Legal/Court'),
    ('social', 'Social'),
    ('other', 'Other'),
]

TRANSLATION_SPECIALIZATION_CHOICES = [
    ('none', 'I don\'t have any specialization'),
    ('standard', 'Standard Translation'),
    ('technical', 'Technical Translation'),
    ('transcreation', 'Transcreation'),
    ('other', 'Other'),
]

PHONE_OS_CHOICES = [
    ('ios', 'IOS (iPhone)'),
    ('android', 'Android'),
    ('microsoft', 'Microsoft'),
    ('blackberry', 'Blackberry'),
    ('other', 'Other'),
]

SKILL_LEVEL_CHOICES = [
    ('poor', 'Poor'),
    ('average', 'Average'),
    ('excellent', 'Excellent'),
]

PAYMENT_METHOD_CHOICES = [
    ('direct_deposit', 'Direct Deposit'),
    ('check', 'Check'),
    ('cash', 'Cash'),
    ('other', 'Other'),
]