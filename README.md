

构造方法01：
=====
public FtpPut(String localFileName, String remoteFileName,String tranCode, FtpClientConfig config)

构造方法02：
=====
public FtpPut(String localFileName, String remoteFileName, String tranCode, boolean scrtFlag, boolean compressFlag, FtpClientConfig config)

构造方法03：
=====
public FtpPut (String localFileName, String remoteFileName, String tranCode, int mode, FtpClientConfig config)


#
方法说明：
=====
“localFileName”本地文件绝对路径，例如：/home/zyb/apps/a.txt；

“remoteFileName”为文件传输系统保存的文件名，例如：test/a.txt；（文件名长度linux限制长度为255，因为文件传输过程中服务端有临时文件，因此文件名长度不要超过255-26=229）

“tranCode”传输交易码，该字段内容请向文件传输系统管理员申请；

“scrtFlag”加密标识，true表示文件加密传输，false表示不加密传输；

“compressFlag”压缩标识，true表示文件压缩传输，false表示不压缩传输；

“mode”传输模式标志，0:普通传输，1：文件加密，2：文件压缩，3：文件加密压缩

“config”，为客户端的配置信息，将FtpClientConfig.properties文件的配置信息进行解析，放入config对象中，配置信息包括文件传输服务器节点的地址、客户端节点地址、用户名以及密码 参考jar包。

请调用doPutFile()方法返回文件传输系统文件保存路径，并按照实际需要通知文件消费系统；

“filePath”返回值表示上传文件的保存路径，例如：/用户名/传输代码/remoteFileName；可以将此返回值发送给文件下载方，依据此文件路径下载对应的文件。
