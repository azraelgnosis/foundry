JOBS = {
    "Hand": {},
    "Land": {},
    "Magic": {
        "Astrologian": {},
        "Black Mage": {},
        "Blue": {},
        "Red Mage": {},
        "Scholar": {},
        "Summoner": {},
        "White Mage": {}
    },
    "War": {
        "Bard": {},
        "Dancer": {},
        "Dark Knight": {},
        "Dragoon": {},
        "Gunbreaker": {},
        "Machinist": {},
        "Monk": {},
        "Ninja": {},
        "Paladin": {},
        "Samurai": {},
        "Warrior": {}
    }
}

class Character:
    __slots__ = ["player", "name", "race", "clan", "jobs", "server", 'avatar', 'portrait']

    def __init__(self, id, name, jobs={}, portrait=None):
        self.name = name
        self.jobs = jobs
        self.portrait = portrait

    #     self._set_jobs()

    # def _set_jobs(self):
    #     for discipline, jobs in JOBS.items():
    #         for job in jobs:
    #             self.jobs[job] = Job(name=job, discipline=discipline)

    def json(self):
        json = {
            'name': self.name,
            'jobs': {
                "Hand": {},
                "Land": {},
                "Magic": {
                    "Astrologian": {},
                    "Black Mage": {},
                    "Blue": {},
                    "Red Mage": {},
                    "Scholar": {},
                    "Summoner": {},
                    "White Mage": {}
                },
                "War": {
                    "Bard": {},
                    "Dancer": {},
                    "Dark Knight": {},
                    ("Lancer", "Dragoon"): {
                        "Log": []
                    },
                    "Gunbreaker": {},
                    "Machinist": {},
                    "Monk": {},
                    "Ninja": {},
                    "Paladin": {},
                    "Samurai": {},
                    "Warrior": {}
                }
            }
        }

        return json

class Job:
    DISCIPLINES = [disciple for disciple in JOBS.keys()]
    JOB_list = [(job for job in JOBS) for discipline, JOBS in JOBS.items()]

    __slots__ = ["name", "discipline", "level", "log", "quests"]

    def __init__(self, name:str, discipline:str):
        self.name = name if name in Job.JOB_list else KeyError
        self.discipline = discipline if discipline in Job.DISCIPLINES else KeyError

        