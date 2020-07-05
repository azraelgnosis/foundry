import click
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3

from foundry.db import DataManager
from foundry.valkyria.models import Row, Soldier, Job, Potential



types = {
    "jobs": Job,
    "potentials": Potential,
    "soldiers": Soldier,
}

class ValkyriaDataManager(DataManager):
    def __init__(self):
        super().__init__('valkyria')
        
    def get_jobs(self) -> list:
        """
        SELECT `jobs`.job_val
            FROM `jobs`
        """

        jobs = self.select('jobs', columns=['job_val'])

        return jobs
   
    def get_potentials(self) -> list:
        """
        SELECT `potentials`.potential_val, `potentials`.potential_text
            FROM `potentials`
        """

        potentials = self.select(
            table='potentials',
            columns=['potential_val', 'potential_text'],
            datatype=Potential)

        return potentials

    def get_soldiers(self) -> list:
        """
        SELECT `soldiers`.soldier_val, `ethnicities`.ethnicity_val, `job`.job_val 
            FROM `soldiers`
            LEFT JOIN `ethnicities` ON `ethnicity`.ethnicity_id = `soldiers`.ethnicity_id
            LEFT JOIN `jobs` ON `jobs`.job_id = `soldiers`.job_id
        """
        
        soldiers = self.select(
            table="soldiers",
            columns=['soldier_val', 'ethnicity_val', 'job_val'],
            join={'ethnicities': ('ethnicity_id'), 'jobs': ('job_id')},
            datatype=Soldier)
            
        return soldiers
