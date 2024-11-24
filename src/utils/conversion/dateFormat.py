from datetime import datetime


def convertToDatetime(date: str) -> datetime:
    """
    Converte string data para objeto datetime
    """
    return datetime.fromisoformat(date)


def convertToIso(date: datetime) -> str:
    """
    Converte objeto datetime para string de data ISO
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')
