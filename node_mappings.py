from .nodes.nodes_core import *
from .nodes.nodes_aspect_ratio import *
from .nodes.nodes_list import *
from .nodes.nodes_sdxl import *
from .nodes.nodes_legacy import *
from .nodes.nodes_utils_index import *
from .nodes.nodes_utils_conversion import *
from .nodes.nodes_utils_random import *
from .nodes.nodes_utils_text import *
from .nodes.nodes_utils_other import *
from .nodes.nodes_lora import *



NODE_CLASS_MAPPINGS = { 
    ### Core Nodes
    "CR Image Output": CR_ImageOutput,
    "CR Latent Batch Size": CR_LatentBatchSize,   
    "CR Conditioning Mixer": CR_ConditioningMixer,
    "CR Select Model": CR_SelectModel,
    "CR Seed": CR_Seed, 
    "CR Prompt Text": CR_PromptText,
    "CR Combine Prompt": CR_CombinePrompt,    
    "CR VAE Decode": CR_VAEDecode,
    ### LoRA Nodes    
    "CR Load LoRA": CR_LoraLoader,    
    "CR LoRA Stack": CR_LoRAStack,
    "CR Random LoRA Stack": CR_RandomLoRAStack,
    "CR Random Weight LoRA": CR_RandomWeightLoRA,
    "CR Apply LoRA Stack": CR_ApplyLoRAStack,  
        
    ### List Nodes
    "CR Text List": CR_TextList,
    "CR Prompt List": CR_PromptList, 
    "CR Simple List": CR_SimpleList,          
    "CR Float Range List": CR_FloatRangeList,
    "CR Integer Range List": CR_IntegerRangeList,
    "CR Load Text List": CR_LoadTextList,
    "CR Binary To Bit List": CR_BinaryToBitList,
    "CR Text Cycler": CR_TextCycler,
    "CR Value Cycler": CR_ValueCycler, 
    ### List IO
    "CR Load Image List": CR_LoadImageList,
    "CR Load Image List Plus": CR_LoadImageListPlus,
    "CR Load GIF As List": CR_LoadGIFAsList,  
    "CR Font File List": CR_FontFileList,      
    ### List Utils
    "CR Batch Images From List": CR_MakeBatchFromImageList,    
    "CR Intertwine Lists" : CR_IntertwineLists,
    "CR Repeater": CR_Repeater,     
    "CR XY Product": CR_XYProduct,  
    "CR Text List To String": CR_TextListToString,   
    ### Aspect Ratio Nodes
    "CR SD1.5 Aspect Ratio": CR_AspectRatioSD15,
    "CR SDXL Aspect Ratio": CR_SDXLAspectRatio,
    "CR Aspect Ratio": CR_AspectRatio,
    "CR Aspect Ratio Banners": CR_AspectRatioBanners, 
    "CR Aspect Ratio Social Media": CR_AspectRatioSocialMedia,  
    "CR_Aspect Ratio For Print": CR_AspectRatioForPrint,
    ### SDXL Nodes
    "CR SDXL Prompt Mix Presets": CR_PromptMixPresets,
    "CR SDXL Style Text": CR_SDXLStyleText,
    "CR SDXL Base Prompt Encoder": CR_SDXLBasePromptEncoder, 
    ### Utils Index
    "CR Index": CR_Index,    
    "CR Index Increment": CR_IncrementIndex,
    "CR Index Multiply": CR_MultiplyIndex,
    "CR Index Reset": CR_IndexReset,
    "CR Trigger": CR_Trigger,
    ### Utils Conversion
    "CR String To Number": CR_StringToNumber,
    "CR String To Combo": CR_StringToCombo,    
    "CR Float To String": CR_FloatToString,
    "CR Float To Integer": CR_FloatToInteger,
    "CR Integer To String": CR_IntegerToString,
    "CR String To Boolean": CR_StringToBoolean,     
    ### Utils Random
    "CR Random Multiline Values": CR_RandomMultilineValues,
    "CR Random Multiline Colors": CR_RandomMultilineColors,    
    "CR Random RGB Gradient": CR_RandomRGBGradient,
    "CR Random Panel Codes": CR_RandomPanelCodes, 
    ### Utils Text 
    "CR Text": CR_Text,    
    "CR Multiline Text": CR_MultilineText,
    "CR Split String": CR_SplitString,     
    "CR Text Concatenate": CR_TextConcatenate, 
    "CR Text Replace": CR_TextReplace,
    "CR Text Length": CR_TextLength,
    "CR Text Operation": CR_TextOperation,  
    "CR Text Blacklist": CR_TextBlacklist,      
    "CR Save Text To File": CR_SaveTextToFile,
    ### Utils Conditional
    "CR Set Value On Boolean": CR_SetValueOnBoolean,
    "CR Set Value On Binary": CR_SetValueOnBinary, 
    "CR Set Value on String": CR_SetValueOnString,
    "CR Set Switch From String": CR_SetSwitchFromString,        
    ### Utils Other     
    "CR Value": CR_Value,
    "CR Integer Multiple": CR_IntegerMultipleOf,
    "CR Clamp Value": CR_ClampValue,     
    "CR Math Operation": CR_MathOperation,
    "CR Get Parameter From Prompt": CR_GetParameterFromPrompt,
    "CR Select Resize Method": CR_SelectResizeMethod,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ### Core Nodes
    "CR Image Output": "💾 CR Image Output",
    "CR Integer Multiple": "⚙️ CR Integer Multiple",
    "CR Latent Batch Size": "⚙️ CR Latent Batch Size", 
    "CR Seed": "🌱 CR Seed",
    "CR Value": "⚙️ CR Value",
    "CR Conditioning Mixer": "⚙️ CR Conditioning Mixer",
    "CR Select Model": "🔮 CR Select Model",
    "CR Prompt Text": "⚙️ CR Prompt Text", 
    "CR Combine Prompt": "⚙️ CR Combine Prompt",
    "CR VAE Decode": "⚙️ CR VAE Decode",  
    ### LoRA Nodes    
    "CR Load LoRA": "💊 CR Load LoRA",    
    "CR LoRA Stack": "💊 CR LoRA Stack",
    "CR Random LoRA Stack": "💊 CR Random LoRA Stack",
    "CR Random Weight LoRA": "💊 CR Random Weight LoRA",
    "CR Apply LoRA Stack": "💊 CR Apply LoRA Stack",   
    ### List Nodes
    "CR Text List": "📜 CR Text List",
    "CR Prompt List": "📜 CR Prompt List",
    "CR Simple List": "📜 CR Simple List",  
    "CR Float Range List": "📜 CR Float Range List",
    "CR Integer Range List": "📜 CR Integer Range List", 
    "CR Load Value List": "📜 CR Load Value List",   
    "CR Load Text List": "📜 CR Load Text List",
    "CR Binary To Bit List": "📜 CR Binary To Bit List",
    "CR Text Cycler": "📜 CR Text Cycler",
    "CR Value Cycler": "📜 CR Value Cycler",
    ### List IO
    "CR Load Image List": "⌨️ CR Load Image List",
    "CR Load Image List Plus": "⌨️ CR Load Image List Plus", 
    "CR Load GIF As List": "⌨️ CR Load GIF As List",
    "CR Font File List": "⌨️ CR Font File List",    
    ### List Utils
    "CR Batch Images From List": "🛠️ CR Batch Images From List",
    "CR Intertwine Lists" : "🛠️ CR Intertwine Lists",
    "CR Repeater": "🛠️ CR Repeater",    
    "CR XY Product": "🛠️ CR XY Product",      
    "CR Text List To String": "🛠️ CR Text List To String",   
    ### Aspect Ratio Nodes
    "CR SD1.5 Aspect Ratio": "🔳 CR SD1.5 Aspect Ratio",
    "CR SDXL Aspect Ratio": "🔳 CR SDXL Aspect Ratio",    
    "CR Aspect Ratio": "🔳 CR Aspect Ratio",
    "CR Aspect Ratio Banners": "🔳 CR Aspect Ratio Banners",
    "CR Aspect Ratio Social Media": "🔳 CR Aspect Ratio Social Media",
    "CR_Aspect Ratio For Print": "🔳 CR_Aspect Ratio For Print",
    ### SDXL Nodes
    "CR SDXL Prompt Mix Presets": "🌟 CR SDXL Prompt Mix Presets",
    "CR SDXL Style Text": "🌟 CR SDXL Style Text",
    "CR SDXL Base Prompt Encoder": "🌟 CR SDXL Base Prompt Encoder", 
    ### Utils Index
    "CR Index":"🔢 CR Index",    
    "CR Index Increment": "🔢 CR Index Increment",
    "CR Index Multiply": "🔢 CR Index Multiply",
    "CR Index Reset": "🔢 CR Index Reset",
    "CR Trigger": "🔢 CR Trigger",
    ### Utils Conversion
    "CR String To Number": "🔧 CR String To Number",
    "CR String To Combo": "🔧 CR String To Combo",    
    "CR Float To String": "🔧 CR Float To String",
    "CR Float To Integer": "🔧 CR Float To Integer",
    "CR Integer To String": "🔧 CR Integer To String", 
    "CR String To Boolean": "🔧 CR String To Boolean",     
    ### Utils Random
    "CR Random Multiline Values": "🎲 CR Random Multiline Values",
    "CR Random Multiline Colors": "🎲 CR Random Multiline Colors",
    "CR Random RGB Gradient": "🎲 CR Random RGB Gradient",
    "CR Random Panel Codes": "🎲 CR Rsandom Panel Codes",
    ### Utils Text
    "CR Text": "🔤 CR Text",
    "CR Multiline Text": "🔤 CR Multiline Text",       
    "CR Split String": "🔤 CR Split String",
    "CR Text Concatenate": "🔤 CR Text Concatenate",
    "CR Text Replace": "🔤 CR Text Replace",
    "CR Text Blacklist": "🔤 Text Blacklist",    
    "CR Text Length": "🔤 CR Text Length",
    "CR Text Operation": "🔤 CR Text Operation", 
    "CR Save Text To File": "🔤 CR Save Text To File",
    ### Utils Conditional
    "CR Set Value On Boolean": "⚙️ CR Set Value On Boolean",
    "CR Set Value On Binary": "⚙️ CR Set Value On Binary",
    "CR Set Value on String": "⚙️ CR Set Value on String",
    "CR Set Switch From String": "⚙️ CR Set Switch From String",     
    ### Utils Other    
    "CR Integer Multiple": "⚙️ CR Integer Multiple",
    "CR Value": "⚙️ CR Value",
    "CR Clamp Value": "⚙️ CR Clamp Value",
    "CR Math Operation": "⚙️ CR Math Operation",
    "CR Get Parameter From Prompt": "⚙️ CR Get Parameter From Prompt",
    "CR Select Resize Method": "⚙️ CR Select Resize Method",
    "CR Select ISO Size": "⚙️ CR Select ISO Size",    
}
