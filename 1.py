data = [
[&#39;Sunny&#39;,&#39;Warm&#39;,&#39;Normal&#39;,&#39;Yes&#39;],
[&#39;Sunny&#39;,&#39;Warm&#39;,&#39;High&#39;,&#39;Yes&#39;],
[&#39;Rainy&#39;,&#39;Cold&#39;,&#39;High&#39;,&#39;No&#39;],
[&#39;Sunny&#39;,&#39;Warm&#39;,&#39;High&#39;,&#39;Yes&#39;]
]
h = [&#39;0&#39;] * (len(data[0]) - 1)
for row in data:
if row[-1] == &#39;Yes&#39;:
if h[0] == &#39;0&#39;:
h = row[:-1]
else:
for i in range(len(h)):
if h[i] != row[i]:
h[i] = &#39;?&#39;
print(h)

print(&quot;Final Hypothesis:&quot;, h)
