from datetime import datetime

def format_date(dt_string):
    dt = datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%SZ")
    return dt


class Team:
    def __init__(self, id, name, shortName, tla, crest):
        self.id = id
        self.name = name
        self.shortName = shortName
        self.tla = tla
        self.crest = crest

class Score:
    def __init__(self, winner, duration, fullTime, halfTime):
        self.winner = winner
        self.duration = duration
        self.fullTime = fullTime
        self.halfTime = halfTime

class Match:
    def __init__(self, homeTeam, awayTeam, score):
        self.homeTeam = Team(**homeTeam)
        self.awayTeam = Team(**awayTeam)
        self.score = Score(**score)

class Filter:
    def __init__(self, dateFrom=None, dateTo=None, competitions=None, permission=None, limit=None):
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        self.permission = permission
        self.limit = limit
        self.competitions = competitions

class ResultSet:
    def __init__(self, count, competitions, first, last, played, wins=None, draws=None, losses=None):
        self.count = count
        self.competitions = competitions
        self.first = first
        self.last = last
        self.played = played
        self.wins = wins
        self.draws = draws
        self.losses = losses

class Area:
    def __init__(self, id, name, code, flag):
        self.id = id
        self.name = name
        self.code = code
        self.flag = flag

class Competition:
    def __init__(self, id, name, code, type, emblem):
        self.id = id
        self.name = name
        self.code = code
        self.type = type
        self.emblem = emblem

class Season:
    def __init__(self, id, startDate, endDate, currentMatchday, winner):
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.currentMatchday = currentMatchday
        self.winner = winner

class Match:
    def __init__(self, area, competition, season, id, utcDate, status, matchday, stage, group, lastUpdated, homeTeam, awayTeam, score, odds, referees):
        self.area = Area(**area)
        self.competition = Competition(**competition)
        self.season = Season(**season)
        self.id = id
        self.utcDate = format_date(utcDate)
        self.status = status
        self.matchday = matchday
        self.stage = stage
        self.group = group
        self.lastUpdated = lastUpdated
        self.homeTeam = Team(**homeTeam)
        self.awayTeam = Team(**awayTeam)
        self.score = Score(**score)
        self.odds = odds
        self.referees = [Referee(**x) for x in referees]

class Referee:
    def __init__(self, id, name, type, nationality):
        self.id = id
        self.name = name
        self.type = type
        self.nationality = nationality

class SoccerData:
    def __init__(self, filters, resultSet, matches):
        self.filters = Filter(**filters)
        self.resultSet = ResultSet(**resultSet)
        self.matches = [Match(**x) for x in matches]




