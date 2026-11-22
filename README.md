# GTA 6 Brands tracker: open data

Every GTA 6 brand move, counted and sourced. Official tie-ins, unofficial brand moves and Rockstar's in-game parody brands, each linked to its source.

370+ entries · 230+ real brands · 170+ publishers cited · updated daily

Site: [gta6brands.com](https://www.gta6brands.com/) · Open data: [gta6brands.com/data](https://www.gta6brands.com/data/) · Developers: [gta6brands.com/developers](https://www.gta6brands.com/developers/)

## Get the data

| File | For |
|---|---|
| [`data/latest/tracker.csv`](data/latest/tracker.csv) | Spreadsheets |
| [`data/latest/tracker.json`](data/latest/tracker.json) | Code |
| [`data/latest/tracker.md`](data/latest/tracker.md) | AI tools |
| [`data/latest/manifest.json`](data/latest/manifest.json) | Counts, fields, checksums |
| [`data/snapshots/`](data/snapshots/) | Dated copies that stay put |
| [`data/changelog.json`](data/changelog.json) | Entries added per day |
| [`tally.json`](tally.json) | Launch-week tally |

```sh
git clone https://github.com/mikelitman/gta6brands-live.git
```

## API

No key. Read-only. JSON. About 60 requests a minute.

```sh
curl "https://www.gta6brands.com/api/v1/brand?name=Nike"
```

| Endpoint | What |
|---|---|
| `/api/v1/brands.json` | Every brand |
| `/api/v1/brands/{slug}.json` | One brand |
| `/api/v1/search?q=` | Search entries |
| `/api/v1/ask?q=` | Ask a question |
| `/api/v1/latest.json` | Latest moves |
| `/api/v1/parodies.json` | In-game parodies |
| `/api/v1/stats.json` | Headline counts |

OpenAPI: [openapi.json](https://www.gta6brands.com/openapi.json)

## MCP

Ask Claude, Cursor or any MCP client. Streamable HTTP, read-only.

```json
{ "mcpServers": { "gta6brands": { "url": "https://www.gta6brands.com/mcp" } } }
```

MCP Registry: `com.gta6brands/tracker`

Tools: `search_brands`, `get_brand`, `latest_moves`, `find_parodies`, `tracker_stats`, `cited_quote`, `latest_number`, `press_chart`.

## Licence

- **Quote it.** Free, with credit, anywhere. Even commercial work and AI answers that link back.
- **Build with it.** Free for personal, research and non-commercial projects.
- **Selling it?** Bulk commercial reuse, or training a commercial AI model on it, needs a licence: hello@mikelitman.me
- **Sources stay theirs.** Every entry links to its publisher.

Full terms: [LICENSE.md](LICENSE.md)

## Cite

> GTA 6 Brands tracker, gta6brands.com, snapshot 22 Nov 2026. https://www.gta6brands.com/data/

Credit "Source: gta6brands.com" with a link. Link each claim to the entry's `source_url`.

## Built something?

Tell us at hello@mikelitman.me and we'll feature it here.

---

Independent, by Mike Litman. Not affiliated with or endorsed by Rockstar Games or Take-Two Interactive. Corrections: hello@mikelitman.me
