Ai-Football

ai-football/
├── main.py - запуск игры 
├── config.py - Конфигурации
├── requirements.txt - Прост библиотеки
│
├── game/
│   ├── engine.py - Основной пайгейм файл для запуска игры
│   ├── pitch.py - Поле
│   ├── ball.py - Мяч
│   ├── player.py - Игроки 
│   ├── rules.py - правила
│   └── match.py - матч
│
├── agents/
│   ├── base_agent.py 
│   ├── rule_based.py
│   └── team_strategy.py
│
├── environment/
│   └── football_env.py
│
├── training/
│   ├── train_ppo.py
│   └── evaluate.py
│
├── analytics/
│   └── match_stats.py
│
└── tests/
    ├── test_rules.py
    └── test_match.py