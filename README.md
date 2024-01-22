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
<p align="center">
  <img src=".github/TX RISK.png" alt="tx risk"/>
</p>

# Report
You can use our predefined templates to report a token, dApp, url or a whole transaction as a scam or mark them as safe using the buttons below!
<p align="center">
<a href="https://github.com/adabox-aio/cardano-shield/issues/new?assignees=adamcazes%2C+Cardano-Shield%2C+hizkiya%2C+ThirdEye707&labels=report+as+scam&projects=&template=report-as-scam.md&title=Scam+Report+-+%5BTransaction+ID%2FDApp%2FURL%2FNFT%5D">
<img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/scam%20button.png?raw=true" alt="report as scam"/></a>
<a href="https://github.com/adabox-aio/cardano-shield/issues/new?assignees=adamcazes%2C+Cardano-Shield%2C+hizkiya%2C+ThirdEye707&labels=mark+as+safe&projects=&template=mark-as-safe.md&title=Mark+as+Safe+-+%5BTransaction+ID%2FDApp%2FURL%2FNFT%5D">
<img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/safe%20button.png?raw=true" alt="Mark as safe"/></a>
</p>
<p align="center">
GeroWallet users can also report a transaction directly from within their wallets History tab
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
# Catalyst Fund10
|<div style="width:400px">Problem</div>|<div style="width:400px">Solution</div>|
|:------------------------------------|:-------|
| Insufficient Safeguards for Wallet Users on Cardano: A Critical Security Gap| Addressing the security challenge by implementing a robust and collaborative security mechanism to protect Cardano wallet users from phishing, low-trust websites, and wallet drainers |

<p align="center">
Cardano Shield Catalyst Milestones
<a href="https://milestones.projectcatalyst.io/projects/1000040">
  <img src="https://github.com/adabox-aio/cardano-shield/blob/main/.github/milestone.png?raw=true" alt="Milestones"/>
</a>

# API Generation (WIP)
While we are preparing our API backend, scheduled for February/March 2024, you can submit a request to receive a Cardano Shield API key.
Please send an email to team@cardanoshield.com or DM us on twitter/discord with your API key request, please include your project name and the API purpose (wallet, community, research, etc)

# Alpha v1.0.7 Known Issues / Bugs
- GeroWallet UI: Tooltips are sometimes janky and not responsive 
- GeroWallet UI: Transactions with decentralized exchanges show 0.0 ADA/Tokens under the "You're receiving" section.
  - While this is intended since the transaction is for creating a Buy/Lend/Stake/etc Order on the exchange and no tokens are expected to be received.

</p>
<p align="center">
    <img src=".github/discordsmall.png" alt="discord">&nbsp;<a href="https://discord.gg/J2ujENSdtm">Discord (adaforge.io)</a>
      |
    <img src=".github/twittersmall.png" alt="Twitter">&nbsp;<a href="https://twitter.com/CardanoShield">Twitter (@CardanoShield)</a>
      |
    <img src=".github/globe.png" alt="Website">&nbsp;<a href="https://www.cardanoshield.com"> Website (cardanoshield.com)</a>
</p>

