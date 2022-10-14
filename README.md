A basic dashbaord to display the API results.

Top table hits the `vehicle_ctr_by_threshold` Endpoint passing the Less Than / Greater Than params, hitting the API every time you change the filter to get the latest results (no local filtering).

The bottom table hits the `vehicle_clicks` Endpoint to get all of the results.

## To run:

```
git clone https://github.com/sdairs/tb_iv_ctr_demo.git
cd tb_iv_ctr_demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard.py
```
