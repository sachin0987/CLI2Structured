# CLI2Structured
Let's Convert CLI Output to Structured , Uses Google TextFSM and PyGenie 


::: mermaid
graph TD;
    Start[Start] --> Retrieve_from_NMDB{Retrieve from NMDB API};
    Retrieve_from_NMDB --> Check_NSO{Check NSO};
    Check_NSO --> |Device Exists| Check_Crosswork{Check Crosswork};
    Check_NSO --> |Device Missing| Add_to_NSO[Add to NSO];
    Check_Crosswork --> |Device Missing| Add_to_Crosswork[Add to Crosswork];
    Add_to_NSO --> Check_Crosswork;
    Add_to_Crosswork --> End[End];
    Check_Crosswork --> End;
:::

find /path/to/your/directory -type f -name 'pattern*' -exec ls -t {} + | tail -n +2 | xargs rm --
