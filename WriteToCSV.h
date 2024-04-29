#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "TextFileEditor.generated.h"

/**
 * 
 */
UCLASS()
class CHARACTERPROJECT_API UTextFileEditor : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "FileEditor")
    static bool SaveTextToCSVFile(FString SaveDirectory, FString FileName, const FString& SaveText, bool AllowOverWriting = false, bool AppendText = false);


};
