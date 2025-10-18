import re
text = "Trending: #AI #2025,not#aHashtag but #deep_learning"
hs = re.findall(r'(^|\s)(#[A-Za-z0-9_]+)', text)
hs = [h[1] for h in hs]
print(hs)