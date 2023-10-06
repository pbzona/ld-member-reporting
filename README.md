# ld-member-activity

This script generates reports for several categories of LaunchDarkly account members that can be
used for seat provisioning and management. This script is *not* maintained or endorsed by LaunchDarkly,
and you are responsible for ensuring your use of the LaunchDarkly API remains in compliance
with any business relationship you have with them.

## Usage

1. Install dependencies in a virtual environment:
    ```sh
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```
2. Copy the `.env.example` file to `.env` and replace the `LD_API_TOKEN` with your own [API Token](https://docs.launchdarkly.com/home/account-security/api-access-tokens)
3. Run the script:
    ```sh
    $ python main.py
    ```
4. Reports will be written to the `reports/` directory. See the `main.py` file for descriptions of what each report entails.
5. Optionally, use the generated reports to [remove inactive members via API](https://apidocs.launchdarkly.com/tag/Account-members#operation/deleteMember).
