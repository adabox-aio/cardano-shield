<p align="center">
<img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/Cardano%20Shield%20logo%20github.png?raw=true" alt="Cardano Shield"/>
</p>

# What is Cardano Shield?
An Open-Source wallet extension backed by Project Catalyst Fund10
Proactive protection from Phishing via websites and transactions using Machine learning modules and community insights.

# Features
- **Malicious Websites Detection**: Advanced URL Analysis Prevents phishing efforts by intercepting them before your wallet is connected.
- **Transaction Summary**: Summarize transactions by providing clear, understandable security information for each transaction, ensuring you are fully aware of potential risks.
- **Transaction Risk Score**: A score is provided based on security checks that run on the transaction before signing it

## Catalyst Fund10
<p align="center">
<a href="https://milestones.projectcatalyst.io/projects/1000040">
  <img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/milestone.png?raw=true" alt="Milestones"/>
</a>
</p>

# Reporting a scam
You can use our predefined templates to report a token, dapp, url transaction as a scam or mark them as safe!
<p align="center">
<a href="https://github.com/adabox-aio/cardano-shield/issues/new?assignees=adamcazes%2C+Cardano-Shield%2C+hizkiya%2C+ThirdEye707&labels=report+as+scam&projects=&template=report-as-scam.md&title=Scam+Report+-+%5BTransaction+ID%2FDApp%2FURL%2FNFT%5D">
  <img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/scam%20button.png?raw=true" alt="report as scam"/>
</a>
  <a href="https://github.com/adabox-aio/cardano-shield/issues/new?assignees=adamcazes%2C+Cardano-Shield%2C+hizkiya%2C+ThirdEye707&labels=mark+as+safe&projects=&template=mark-as-safe.md&title=Mark+as+Safe+-+%5BTransaction+ID%2FDApp%2FURL%2FNFT%5D">
  <img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/safe%20button.png?raw=true" alt="Mark as safe"/>
</a>
</p>

# Blacklist & Whitelist
We maintain both a blacklist and whitelist and update them frequently based on community feedback and our ML analysis.
if you wish to modify or add a new entry to these files using a PR, please follow the following file structure:

### Tokens:
```json
{
  "policies":{
    "SCAM Token Name":"policy-id",
}
```
### Domains:
```json
  "domains":[
    "scamdomain.com",
]
```
### Stake Address:
```json
 "stake":[
    "fakestake1u83ane6luhljcl59e54jlm7u44agpnxuc5uanl9nfvj794quy",
  ]
```

<p style="text-align: center">
    <a href="https://discord.gg/J2ujENSdtm"><img src=".github/discordsmall.png" alt="Twitter">Discord (adaforge.io)</a>
      |
    <a href="https://twitter.com/CardanoShield"><img src=".github/twittersmall.png" alt="Twitter">Twitter (@CardanoShield)</a>
      |
  <a href="https://www.cardanoshield.com"> Website (cardanoshield.com)</a>
</p>
