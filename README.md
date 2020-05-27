## Algo Functions 👨🏿‍💻

Everyday, I try to solve at least one algorithm challenge. These challenges are provided by [Daily Coding Problem](https://www.dailycodingproblem.com/). Over time, they have helped me hone my algo skills and I felt I should share the usage of those I find interesting. I did not want to create a standard web app for this, so I decided to use Azure Serverless Functions.

Most of the endpoints will be post requests expecting some data in relation to the challenge.

### How to use

Each endpoint has a specific format of data it is expecting in order to return the appropriate result. Some accommodations have been made for errors on the part of the user.

**Locally**

- Clone this repo
- Install Azure Function Core Tools if you haven't. [Find help here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#v2)
- Run `func start`

**Public Cloud**

- Follow instructions below using `https://iyikuyoroalgofunc.azurewebsites.net` as the `baseURL`

### Endpoints Instructions

- [SudokuSolver](https://github.com/IyiKuyoro/AlgoEndpoints-Azure-Serverless-Functions-/blob/master/SudokuFunction/README.md)

### Response Format

Most responses will have the following format:
json
```
{
    success: type Boolean,
    message: type String,
    errors: type String[] | data: type Object
}
```
