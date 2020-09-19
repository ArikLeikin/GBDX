
1.GBDX Images Downloader tool must have a gbdxtools config file in order to work:

***[CONTENT]***
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[gbdx]
auth_url = https://geobigdata.io/auth/v1/oauth/token/
client_id = B9tFshItGFxqRGL3a;zZd4GZsQ7FTX!lZbk9FE6C
client_secret = _DNm_zKbK!3Qx_ugKmWeOh;g8ZGBZLy2v!N?hG8nJzNPa1O_ec7Gua?k3cqr2sjWTPRg27Qe7q5PK5y889ID.qLrNbB8N96g.Y4Qj@yWG6411o16-WmIZzvWXkC7F.rN
user_name = lahavy@video-inform.com
user_password = 5642296Yeffet7

[gbdx_token]
json = {"access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1Ea3hPREE1UTBFeFJUTXpOek01UlVSRE5qWTRRelpHT1ROR1FUWTBNMFJHTnpjMFEwTTFSZyJ9.eyJodHRwczovL2dlb2JpZ2RhdGEuaW8vYWNjb3VudF9sZXZlbCI6ImN1c3RvbSIsImh0dHBzOi8vZ2VvYmlnZGF0YS5pby9pZCI6ImZjY2NlMDA2LTU2ZWQtNDViNC1iZTU0LWFkNzIzOTJiODdlMCIsImh0dHBzOi8vZ2VvYmlnZGF0YS5pby9hY2NvdW50X2lkIjoiMzRjYTc4M2MtYzc5Mi00ZjAzLWExMDAtNTE5M2QwMmUzOTJjIiwiaHR0cHM6Ly9nZW9iaWdkYXRhLmlvL3JvbGVzIjpbInVzZXIiXSwiaHR0cHM6Ly9nZW9iaWdkYXRhLmlvL2VtYWlsIjoibGFoYXZ5QHZpZGVvLWluZm9ybS5jb20iLCJpc3MiOiJodHRwczovL2RpZ2l0YWxnbG9iZS1wcm9kdWN0aW9uLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ODJhYjQ1NjhjNzI2ZDRiMDM0MjFhYTMiLCJhdWQiOlsiZ2VvYmlnZGF0YS5pbyIsImh0dHBzOi8vZGlnaXRhbGdsb2JlLXByb2R1Y3Rpb24uYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5OTk5MDA2OCwiZXhwIjoxNjAwNTk0ODY4LCJhenAiOiJkYnhVNWNaZGtPMFNIVG1zaEZDV25JODk0dnhRMU5ieiIsInNjb3BlIjoib3BlbmlkIGVtYWlsIG9mZmxpbmVfYWNjZXNzIiwiZ3R5IjpbInJlZnJlc2hfdG9rZW4iLCJwYXNzd29yZCJdfQ.1bELjyAVUPUxHfZWbB_I87arBlFzHeA442Sza0-uii9kDZ7EpVtkh2mLlop4xjCPHCjD_QF5vyA0ybYqKvfRQL5Y5m8dN2yxcV9kMBTWu9R5JGbCfdobY7BtJup447kyyHFjHYe7aGGRu7QgK6YC7Rmj9RfWRZvI4WaCtehO9pj-vJzDmu_J5ATz9EnsoaztT6toYvLXHiQhI5GF8H96zwn4tMhVpNd5Ghystvk3MFqaiUDzXmCaerXTlAe8_GcoFOeVq2h_0Rn1CQJg08x8DSBh3nH64DKyCoyVW_fsToVrM0xrZ0Fu6SBfFq3bT0pNlNxBR8y0of5T8XUK80zfWw", "expires_in": 604800, "token_type": "Bearer", "scope": ["openid", "email", "offline_access"], "expires_at": 1600594868.90397, "refresh_token": "EUosjCxT0iamdz2QIb3CU0UBXJhMxDyb_zaz1Q_gSJZpB"}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***[end]***

Copy ".gbdx-config" file to "C:\Users\<username>".

2.AOI coordinate (Crop) format-wkt:

"POLYGON ((longtitude1 latitude1, longtitude2 latitude2, longtitude3 latitude3, longtitude4 latitude4, longtitude1 latitude1))"

example:

"POLYGON((56.335213571289046 25.217757840251576,56.335385232666 25.176906771954453,56.36611261914061 25.17628535715365,56.36559763500975 25.21806844224977,56.335213571289046 25.217757840251576))"

Generate coordinates with HPI Polygon Tool - http://apps.headwallphotonics.com/