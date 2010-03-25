#ifndef CATCHMENTCSS_H
#define CATCHMENTCSS_H

#include <node.h>
#include <vector>
#include <map>
#include <flow.h>

CD3_DECLARE_NODE(CatchmentCSS)
public:
	CatchmentCSS();
	virtual ~CatchmentCSS();
	int f(ptime time, int dt);
	bool init(ptime start, ptime end, int dt);
	void deinit();
private:
	void addMuskParam(int dt);
	void setMuskParam(double *C_x, double *C_y, int dt);
	void initFlows();

	Flow rain_in, dwf_in, parasite_in, q_upstream, out; //ports

	Flow loss_basin; //states
	std::vector<Flow *> V;
	int area;
	double run_off_coeff;
	double initial_loss;
	double permanent_loss;
	int N;
	double K, X;
	std::vector<double> rain_concentration;

	std::map<int, std::pair<double, double> > musk_param;
	ptime start;
};

#endif // CATCHMENTCSS_H
