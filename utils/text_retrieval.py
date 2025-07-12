import json
from sentence_transformers import SentenceTransformer, util

class TextRetrieval:
    def __init__(self):
        # Load embedding model
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def event_recommender(self, events, user_interests, top_n=10):
        interest_embedding = self.model.encode(user_interests)

        # Prepare event descriptions
        for event in events:
            tags = event['tags']
            if isinstance(tags, list):
                tags_str = ", ".join(tags)
            elif isinstance(tags, str):
                tags_str = tags
            else:
                tags_str = ""
            event_text = event['title'] + ". " + event['description'] + ". " + tags_str
            event['embedding'] = self.model.encode(event_text)

        # Compute similarities
        scored_events = []
        for event in events:
            score = util.cos_sim(event['embedding'], interest_embedding)
            event['score'] = score[0][0]
            scored_events.append(event)

        # Sort by score
        scored_events.sort(key=lambda x: x['score'], reverse=True)

        return scored_events[:top_n]


