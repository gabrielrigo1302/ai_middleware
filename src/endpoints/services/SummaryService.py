class SummaryService:
    def __init__(self):
        pass
    
    async def summarize(self, conversation_id: str, max_tokens: str) -> str:
        return conversation_id + " summarized with tokens " + str(max_tokens)   