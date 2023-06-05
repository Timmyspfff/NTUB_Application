// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:dio/dio.dart';
import 'package:dio_cookie_manager/dio_cookie_manager.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:cookie_jar/cookie_jar.dart';

Future<void> main() async {
  Dio dio = Dio();
  CookieJar cookieJar = CookieJar();
  dio.interceptors.add(CookieManager(cookieJar));

  var response = await dio.get('https://ntcbadm1.ntub.edu.tw/login.aspx');
  print(await cookieJar
      .loadForRequest(Uri.parse('https://ntcbadm1.ntub.edu.tw/login.aspx')));
  var responseBody = response.data;
  print(responseBody);
  // await dio.post('https://ntcbadm1.ntub.edu.tw/login.aspx');
}
