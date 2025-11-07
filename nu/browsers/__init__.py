"""Módulos BrowserWorkers de Nu"""

from .base_worker import BrowserWorker
from .freelancer_worker import FreelancerWorker
from .upwork_worker import UpworkWorker
from .github_worker import GitHubWorker

__all__ = [\'BrowserWorker\', \'FreelancerWorker\', \'UpworkWorker\', \'GitHubWorker\']
