import java.awt.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Set;

import com.sun.jna.Pointer;
import com.sun.jna.ptr.*;


/** 
* Based on the original EmoState example with modifications
*
* The main class that handles getting data from Emo device
* or from Emo Emulator (AKA EmoComposer), sanitize it,
* encode it and send it to the server.
* use option - 1 for Emotiv device
*            - 2 for Emotic emulator (AKA EmoComposer)
* Set targetURL for your site data collection method
*/
public class EmoStateLog 
{      

    public static void main(String[] args) 
    {
    	Pointer eEvent			= Edk.INSTANCE.EE_EmoEngineEventCreate();
    	Pointer eState			= Edk.INSTANCE.EE_EmoStateCreate();
    	IntByReference userID 	= null;
    	short composerPort		= 1726;
    	int option 				= 2;
    	int state  				= 0;
    	String targetURL = "http://neurobrush.com/collect";
    	//String targetURL = "http://localhost:8000/collect";
    	
    	HashMap<String,String> dataToSend = new HashMap<String,String>();
    	
    	userID = new IntByReference(0);
    	System.out.println("Starting EmoState...");
    	switch (option) {
		case 1:
		{
			if (Edk.INSTANCE.EE_EngineConnect("Emotiv Systems-5") != EdkErrorCode.EDK_OK.ToInt()) {
				System.out.println("Emotiv Engine start up failed.");
				return;
			}
			break;
		}
		case 2:
		{
			System.out.println("Target IP of EmoComposer: [127.0.0.1] ");

			if (Edk.INSTANCE.EE_EngineRemoteConnect("127.0.0.1", composerPort, "Emotiv Systems-5") != EdkErrorCode.EDK_OK.ToInt()) {
				System.out.println("Cannot connect to EmoComposer on [127.0.0.1]");
				return;
			}
			System.out.println("Connected to EmoComposer on [127.0.0.1]");
			break;
		}
		default:
			System.out.println("Invalid option...");
			return;
    	}
    	
		while (true) 
		{
			state = Edk.INSTANCE.EE_EngineGetNextEvent(eEvent);

			// New event needs to be handled
			if (state == EdkErrorCode.EDK_OK.ToInt()) {

				int eventType = Edk.INSTANCE.EE_EmoEngineEventGetType(eEvent);
				Edk.INSTANCE.EE_EmoEngineEventGetUserId(eEvent, userID);

				// Log the EmoState if it has been updated
				if (eventType == Edk.EE_Event_t.EE_EmoStateUpdated.ToInt()) {

					Edk.INSTANCE.EE_EmoEngineEventGetEmoState(eEvent, eState);
					float timestamp = EmoState.INSTANCE.ES_GetTimeFromStart(eState);
					System.out.println(timestamp + " : New EmoState from user " + userID.getValue());
					
					System.out.print("WirelessSignalStatus: ");
					System.out.println(EmoState.INSTANCE.ES_GetWirelessSignalStatus(eState));
					
					//smile
					float smile = EmoState.INSTANCE.ES_ExpressivGetSmileExtent(eState);
					System.out.println(smile);
					dataToSend.put("Lowerface","'Smile'");
					dataToSend.put("LowerfaceValue", String.valueOf(smile));
					
					if (EmoState.INSTANCE.ES_ExpressivIsLeftWink(eState) == 1) {
						dataToSend.put("Upperface","'LeftWink'");
						float power = EmoState.INSTANCE.ES_ExpressivGetLowerFaceActionPower(eState);
						System.out.println("LeftWink");
						dataToSend.put("UpperfaceValue",String.valueOf(power));
					}
					
					if (EmoState.INSTANCE.ES_ExpressivIsRightWink(eState) == 1) {
						dataToSend.put("Upperface","'RightWink'");
						float power = EmoState.INSTANCE.ES_ExpressivGetLowerFaceActionPower(eState);
						System.out.println("RightWink");
						dataToSend.put("UpperfaceValue",String.valueOf(power));
					}
					
					if (EmoState.INSTANCE.ES_ExpressivIsBlink(eState) == 1) {
						dataToSend.put("Upperface","'Blink'");
						float power = EmoState.INSTANCE.ES_ExpressivGetLowerFaceActionPower(eState);
						System.out.println("'Blink'");
						dataToSend.put("UpperfaceValue",String.valueOf(power));
					}
					
					if (EmoState.INSTANCE.ES_ExpressivIsLookingRight(eState) == 1)
						System.out.println("LookingLeft");
					if (EmoState.INSTANCE.ES_ExpressivIsLookingLeft(eState) == 1)
						System.out.println("LookingRight");
					
					System.out.print("ExcitementShortTerm: ");
					float excitment = EmoState.INSTANCE.ES_AffectivGetExcitementShortTermScore(eState);
					System.out.println(excitment);
					dataToSend.put("ExcitementShortTerm", String.valueOf(excitment));
					
					System.out.print("ExcitementLongTerm: ");
					float excitmentLongTerm = EmoState.INSTANCE.ES_AffectivGetExcitementLongTermScore(eState);
					System.out.println(excitmentLongTerm);
					dataToSend.put("ExcitementLongTerm", String.valueOf(excitmentLongTerm));
					
					System.out.print("EngagementBoredom: ");
					float engagementBoredom = EmoState.INSTANCE.ES_AffectivGetEngagementBoredomScore(eState);
					System.out.println(excitmentLongTerm);
					dataToSend.put("EngagementBoredom", String.valueOf(engagementBoredom));
					
					System.out.print("FrustrationScore: ");
					float frustrationScore = EmoState.INSTANCE.ES_AffectivGetFrustrationScore(eState);
					System.out.println(excitmentLongTerm);
					dataToSend.put("FrustrationScore", String.valueOf(frustrationScore));
					
					System.out.print("Is Eye Open:");
					System.out.println(EmoState.INSTANCE.ES_ExpressivIsEyesOpen(eState));
					
					//create string

					String urlParams = "{";
					for (Entry<String, String> entry : dataToSend.entrySet()) {
						urlParams = urlParams + "'" + entry.getKey() + "':";
						urlParams = urlParams + entry.getValue() + ",";
					}
					urlParams = urlParams.substring(0,urlParams.length()-1) + "}";
					
					System.out.println(urlParams);
					
					System.out.println("Sending to server...");
					Sender.excutePost(targetURL, urlParams);

				}
			}
			else if (state != EdkErrorCode.EDK_NO_EVENT.ToInt()) {
				System.out.println("Internal error in Emotiv Engine!");
				break;
			}
		}
    	
    	Edk.INSTANCE.EE_EngineDisconnect();
    	System.out.println("Disconnected!");
    }
}
