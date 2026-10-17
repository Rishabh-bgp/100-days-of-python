# Cafe & Wifi API (local)

Base URL: `http://127.0.0.1:5000`

| Method | Path | Params | Description |
|---|---|---|---|
| GET | `/random` | none | One random cafe |
| GET | `/all` | none | All cafes, sorted by name |
| GET | `/search` | `loc` | Cafes whose location contains `loc` (404 if none) |
| POST | `/add` | form: `name, map_url, img_url, loc, seats, toilet, wifi, sockets, calls, coffee_price` | Add a cafe (201) |
| PATCH | `/update-price/<id>` | `new_price` | Update coffee price (404 if the id is unknown) |
| DELETE | `/report-closed/<id>` | `api-key` query or `X-API-Key` header | Delete a cafe (403 with a wrong key) |

Examples:

```bash
curl http://127.0.0.1:5000/random
curl "http://127.0.0.1:5000/search?loc=MG"
curl -X PATCH "http://127.0.0.1:5000/update-price/1?new_price=₹200"
curl -X DELETE -H "X-API-Key: TopSecretAPIKey" http://127.0.0.1:5000/report-closed/3
```

The key is a local demo value (`CAFE_API_KEY` env var). It's checked by your own app, not an external service.
