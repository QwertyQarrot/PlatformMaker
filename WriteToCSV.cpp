#include "TextFileEditor.h"
#include "Misc/FileHelper.h"
#include "HAL/PlatformFilemanager.h"

bool UTextFileEditor::SaveTextToCSVFile(FString SaveDirectory, FString FileName, const FString& SaveText, bool AllowOverWriting, bool AppendText)
{
    // Set complete file path
    FString FullPath = FPaths::Combine(SaveDirectory, FileName);

    // Check if overwriting is allowed and if the file already exists
    if (!AllowOverWriting && FPlatformFileManager::Get().GetPlatformFile().FileExists(*FullPath))
    {
        return false; // File already exists and overwriting is not allowed
    }

    FString FinalString;

    if (AppendText)
    {
        // Read existing text from the file
        FString ExistingText;
        if (FFileHelper::LoadFileToString(ExistingText, *FullPath))
        {
            // Concatenate existing text with new text
            FinalString = ExistingText + SaveText;
        }
        else
        {
            // Failed to read existing text, use only the new text
            FinalString = SaveText;
        }
    }
    else
    {
        // If AppendText is false, use only the new text
        FinalString = SaveText;
    }

    // Save FinalString to file
    return FFileHelper::SaveStringToFile(FinalString, *FullPath);
}


