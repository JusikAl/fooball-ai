Ai-Football

ai-football/
├── main.py
├── config.py
├── requirements.txt
│
├── game/
│   ├── engine.py
│   ├── pitch.py
│   ├── ball.py
│   ├── player.py
│   ├── rules.py
│   └── match.py
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