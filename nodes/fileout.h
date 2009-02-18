#ifndef FILEOUT_H
#define FILEOUT_H

#include <node.h>
class QFile;
class QTextStream;

CD3_DECLARE_NODE(FileOut)
public:
	FileOut();
	~FileOut();
	virtual void f(int time, int dt);
	virtual void init(int start, int stop, int dt);
	virtual void deinit();
private:
	Flow *in;
	std::string *out_file_name;
	QFile *file;
	QTextStream *stream;
};

#endif // FILEOUT_H
