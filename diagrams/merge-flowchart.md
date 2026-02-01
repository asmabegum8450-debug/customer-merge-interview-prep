flowchart TD
    A([Start]) --> B[Set i = m-1, j = n-1, k = m+n-1]
    B --> C{Is j >= 0?}
    C -- No --> Z([Done])
    C -- Yes --> D{Is i >= 0 AND customerData1[i] > customerData2[j]?}
    D -- Yes --> E[customerData1[k] = customerData1[i]]
    E --> F[i--]
    F --> G[k--]
    G --> C
    D -- No --> H[customerData1[k] = customerData2[j]]
    H --> I[j--]
    I --> J[k--]
    J --> C
