# xls2csv-server

Call `libreoffice` and `xlsx2csv` via HTTP.

## Usage

```shell
curl \
    -F "sheet=2" \
    -F "file=@your-awesome-spreadsheet.xls" \
    -o output.csv
    http://127.0.0.1:5001/
```

## API Reference

- `POST /`
  - Parameters
    - `file` — XLS file as `multipart/form-data`
    - `sheet` (`number` optional) — index of the sheets
  - Response
    - `text/csv`

## Contributing

If you have any ideas let @nobuf know by opening an issue. Pull requests are warmly welcome.

## License

MIT