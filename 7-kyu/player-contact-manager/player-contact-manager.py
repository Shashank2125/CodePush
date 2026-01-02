def player_manager(players):
    if not players:
        return []
    parts=[p.strip() for p in players.split(",")]
    result=[]
    for i in range(0,len(parts),2):
        result.append({
            "player":parts[i],
            "contact":int(parts[i+1])
        })
    return result