# flows/daily_loop.py
def daily_loop():
    # Stub: orchestrates end-to-end flow; replace with CrewAI graph
    from agents.market_hunter import run as hunt
    from agents.persona_forge import run as forge
    from agents.content_producer import run as produce
    from agents.monetization import run as monetize
    from agents.uploader import run as upload
    from agents.analytics_pivot import run as analyze
    from agents.back_office import run as backoffice

    niche = hunt()
    persona = forge(niche)
    assets = produce(persona, niche)
    linked = monetize(assets)
    posted = upload(linked)
    actions = analyze(posted)
    report = backoffice(actions)
    return report
