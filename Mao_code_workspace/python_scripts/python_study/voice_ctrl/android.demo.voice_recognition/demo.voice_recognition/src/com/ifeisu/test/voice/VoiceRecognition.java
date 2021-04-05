package com.ifeisu.test.voice;

import java.util.ArrayList;
import java.util.List;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
/***
 * 语音识别demo,在使用此demo之前需要确认手机或者模拟器上安装了google的语音搜索工具
 * Voice_Search_2.1.4.apk或者更高版本
 * @author guoxinzz@163.com
 * @website http://www.ifeisu.com
 *
 */
public class VoiceRecognition extends Activity implements OnClickListener {

	private static final int VOICE_RECOGNITION_REQUEST_CODE = 1234;

	private ListView mList;

	/**
	 * 
	 * Called with the activity is first created.
	 */

	@Override
	public void onCreate(Bundle savedInstanceState)

	{

		super.onCreate(savedInstanceState);

		setContentView(R.layout.main);

		Button speakButton = (Button) findViewById(R.id.btn_speak);

		mList = (ListView) findViewById(R.id.list);

		// Check to see if a recognition activity is present

		PackageManager pm = getPackageManager();

		List<ResolveInfo> activities = pm.queryIntentActivities(new Intent(
				RecognizerIntent.ACTION_RECOGNIZE_SPEECH), 0);

		if (activities.size() != 0)

		{

			speakButton.setOnClickListener(this);

		}

		else

		{

			speakButton.setEnabled(false);

			speakButton.setText("Recognizer not present");

		}

	}

	public void onClick(View v)

	{

		if (v.getId() == R.id.btn_speak)

		{

			startVoiceRecognitionActivity();

		}

	}

	private void startVoiceRecognitionActivity()

	{

		// 通过Intent传递语音识别的模式

		Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
		// 语言模式和自由形式的语音识别

		intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
				RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);

		// 提示语音开始

		intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
				"请说出需要打开的网站名字.");

		// 开始执行我们的Intent、语音识别

		startActivityForResult(intent, VOICE_RECOGNITION_REQUEST_CODE);

	}

	// 当语音结束时的回调函数onActivityResult

	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data)

	{

		if (requestCode == VOICE_RECOGNITION_REQUEST_CODE
				&& resultCode == RESULT_OK)

		{

			// 取得语音的字符

			ArrayList<String> matches = data
					.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);

			mList.setAdapter(new ArrayAdapter<String>(this,
					android.R.layout.simple_list_item_1, matches));

		}

		super.onActivityResult(requestCode, resultCode, data);

	}

}
