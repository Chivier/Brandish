# Brandish

Brandish is a Web-based application to display 3D geometry data.

## How to start Brandish Frontend?

```bash
npm install
npm test
```

## How to generate Brandish data?

1. Download data from `resources/fulldata_url.txt`
2. (Optional) Create python virtual environment.
3. Execute:
    ```bash
    pip install -r requirements.txt
    python nc_file_parser.py
    ```

## Brandish Framwork

![frame](doc/image/frame.svg)

## Working Process
- [x] Netcdf format parsing
- [ ] GIS format parsing
- [ ] Json file generating
- [ ] Echarts show 3D scalar field
- [ ] Echarts show 3D vector field (flow field)
- [ ] Deploy on server