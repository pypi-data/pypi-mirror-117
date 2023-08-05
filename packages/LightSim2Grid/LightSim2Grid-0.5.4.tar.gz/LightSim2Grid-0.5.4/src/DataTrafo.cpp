// Copyright (c) 2020, RTE (https://www.rte-france.com)
// See AUTHORS.txt
// This Source Code Form is subject to the terms of the Mozilla Public License, version 2.0.
// If a copy of the Mozilla Public License, version 2.0 was not distributed with this file,
// you can obtain one at http://mozilla.org/MPL/2.0/.
// SPDX-License-Identifier: MPL-2.0
// This file is part of LightSim2grid, LightSim2grid implements a c++ backend targeting the Grid2Op platform.

#include "DataTrafo.h"
#include <iostream>
#include <sstream>

void DataTrafo::init(const RealVect & trafo_r,
                           const RealVect & trafo_x,
                           const CplxVect & trafo_b,
                           const RealVect & trafo_tap_step_pct,
            //                        const RealVect & trafo_tap_step_degree,
                           const RealVect & trafo_tap_pos,
                           const RealVect & trafo_shift_degree,
                           const std::vector<bool> & trafo_tap_hv,  // is tap on high voltage (true) or low voltate
                           const Eigen::VectorXi & trafo_hv_id,
                           const Eigen::VectorXi & trafo_lv_id
                           )
{
    /**
    INPUT DATA ARE ALREADY PAIR UNIT !!
    DOES NOT WORK WITH POWERLINES
    **/
    int size = trafo_r.size();
    DataGeneric::check_size(trafo_r, size, "trafo_r");
    DataGeneric::check_size(trafo_x, size, "trafo_x");
    DataGeneric::check_size(trafo_b, size, "trafo_b");
    DataGeneric::check_size(trafo_tap_step_pct, size, "trafo_tap_step_pct");
    DataGeneric::check_size(trafo_tap_pos, size, "trafo_tap_pos");
    DataGeneric::check_size(trafo_shift_degree, size, "trafo_shift_degree");
    DataGeneric::check_size(trafo_tap_hv, static_cast<std::vector<bool>::size_type>(size), "trafo_tap_hv");
    DataGeneric::check_size(trafo_hv_id, size, "trafo_hv_id");
    DataGeneric::check_size(trafo_lv_id, size, "trafo_lv_id");

    //TODO "parrallel" in the pandapower dataframe, like for lines, are not handled. Handle it python side!

    RealVect ratio = my_one_ + 0.01 * trafo_tap_step_pct.array() * trafo_tap_pos.array();
//    for(int i = 0; i < trafo_tap_hv.size(); ++i)
//    {
//        // in the equation i do as if the ratio was on the lv side (so ratio = hv / lv) if it's given in
//        // the lv side, i need to invert it.
//        if(!trafo_tap_hv[i]) ratio[i] = my_one_ / ratio[i];
//    }
    r_ = trafo_r;
    x_ = trafo_x;
    h_ = trafo_b;
    ratio_ = ratio;
    shift_ = trafo_shift_degree / 180. * my_pi;  // do not forget conversion degree / rad here !
    bus_hv_id_ = trafo_hv_id;
    bus_lv_id_ = trafo_lv_id;
    is_tap_hv_side_ = trafo_tap_hv;
    status_ = std::vector<bool>(trafo_r.size(), true);
}

DataTrafo::StateRes DataTrafo::get_state() const
{
     std::vector<real_type> branch_r(r_.begin(), r_.end());
     std::vector<real_type> branch_x(x_.begin(), x_.end());
     std::vector<cplx_type> branch_h(h_.begin(), h_.end());
     std::vector<int > bus_hv_id(bus_hv_id_.begin(), bus_hv_id_.end());
     std::vector<int > bus_lv_id(bus_lv_id_.begin(), bus_lv_id_.end());
     std::vector<bool> status = status_;
     std::vector<real_type> ratio(ratio_.begin(), ratio_.end());
     std::vector<real_type> shift(shift_.begin(), shift_.end());
     std::vector<bool> is_tap_hv_side = is_tap_hv_side_;
     DataTrafo::StateRes res(branch_r, branch_x, branch_h, bus_hv_id, bus_lv_id, status, ratio, is_tap_hv_side, shift);
     return res;
}
void DataTrafo::set_state(DataTrafo::StateRes & my_state)
{
    reset_results();

    std::vector<real_type> & branch_r = std::get<0>(my_state);
    std::vector<real_type> & branch_x = std::get<1>(my_state);
    std::vector<cplx_type> & branch_h = std::get<2>(my_state);
    std::vector<int> & bus_hv_id = std::get<3>(my_state);
    std::vector<int> & bus_lv_id = std::get<4>(my_state);
    std::vector<bool> & status = std::get<5>(my_state);
    std::vector<real_type> & ratio = std::get<6>(my_state);
    std::vector<bool> & is_tap_hv_side = std::get<7>(my_state);
    std::vector<real_type> & shift = std::get<8>(my_state);

    auto size = branch_r.size();
    DataGeneric::check_size(branch_r, size, "branch_r");
    DataGeneric::check_size(branch_x, size, "branch_x");
    DataGeneric::check_size(branch_h, size, "branch_h");
    DataGeneric::check_size(bus_hv_id, size, "bus_hv_id");
    DataGeneric::check_size(bus_lv_id, size, "bus_lv_id");
    DataGeneric::check_size(status, size, "status");
    DataGeneric::check_size(ratio, size, "ratio");
    DataGeneric::check_size(is_tap_hv_side, size, "is_tap_hv_side");
    DataGeneric::check_size(shift, size, "shift");

    // now assign the values
    r_ = RealVect::Map(&branch_r[0], size);
    x_ = RealVect::Map(&branch_x[0], size);
    h_ = CplxVect::Map(&branch_h[0], size);

    // input data
    bus_hv_id_ = Eigen::VectorXi::Map(&bus_hv_id[0], size);
    bus_lv_id_ = Eigen::VectorXi::Map(&bus_lv_id[0], size);
    status_ = status;
    ratio_  = RealVect::Map(&ratio[0], size);
    shift_  = RealVect::Map(&shift[0], size);
    is_tap_hv_side_ = is_tap_hv_side;
}

void DataTrafo::fillYbus_spmat(Eigen::SparseMatrix<cplx_type> & res, bool ac, const std::vector<int> & id_grid_to_solver)
{
    throw std::runtime_error("fillYbus_spmat is no longer used nor updated !");
    //TODO this is no more used!!!! see the other fillYbus

    //TODO merge that with fillYbusBranch!
    //TODO template here instead of "if"
    int nb_trafo = nb();
    for(int trafo_id =0; trafo_id < nb_trafo; ++trafo_id){
        // i don't do anything if the trafo is disconnected
        if(!status_[trafo_id]) continue;

        // compute from / to
        int bus_hv_id_me = bus_hv_id_(trafo_id);
        int bus_hv_solver_id = id_grid_to_solver[bus_hv_id_me];
        if(bus_hv_solver_id == _deactivated_bus_id){
            throw std::runtime_error("DataModel::fillYbusTrafo: A trafo is connected (hv) to a disconnected bus.");
        }
        int bus_lv_id_me = bus_lv_id_(trafo_id);
        int bus_lv_solver_id = id_grid_to_solver[bus_lv_id_me];
        if(bus_lv_solver_id == _deactivated_bus_id){
            throw std::runtime_error("DataModel::fillYbusTrafo: A trafo is connected (lv) to a disconnected bus.");
        }
        //TODO this is no more used!!!! see the other fillYbus

        // get the transformers ratio
        real_type r = ratio_(trafo_id);

        // subsecptance
        cplx_type h = {my_zero_, my_zero_} ;
        if(ac){
            h = h_(trafo_id);
            h = my_i * my_half_ * h;
        }
        //TODO this is no more used!!!! see the other fillYbus

        // admittance
        cplx_type y = 0.;
        cplx_type z = x_(trafo_id);
        if(ac){
            z *= my_i;
            z += r_(trafo_id);
        }
        if(z != my_zero_) y = my_one_ / z;
       //TODO this is no more used!!!! see the other fillYbus
        // fill non diagonal coefficient
        cplx_type tmp = y / r;
        res.coeffRef(bus_hv_solver_id, bus_lv_solver_id) -= tmp ;
        res.coeffRef(bus_lv_solver_id, bus_hv_solver_id) -= tmp;

        // fill diagonal coefficient
        if(!ac){
            r = my_one_; // in dc, r = 1.0 here (same voltage both side)
        }
        //TODO this is no more used!!!! see the other fillYbus
        tmp += h;
        res.coeffRef(bus_hv_solver_id, bus_hv_solver_id) += tmp / r;
        res.coeffRef(bus_lv_solver_id, bus_lv_solver_id) += tmp * r;
    }
}

void DataTrafo::fillYbus(std::vector<Eigen::Triplet<cplx_type> > & res,
                         bool ac,
                         const std::vector<int> & id_grid_to_solver,
                         real_type sn_mva)
{
    //TODO merge that with fillYbusBranch!
    //TODO template here instead of "if" for ac / dc
    int nb_trafo = nb();
    for(int trafo_id =0; trafo_id < nb_trafo; ++trafo_id){
        // i don't do anything if the trafo is disconnected
        if(!status_[trafo_id]) continue;

        // compute from / to
        int bus_hv_id_me = bus_hv_id_(trafo_id);
        int bus_hv_solver_id = id_grid_to_solver[bus_hv_id_me];
        if(bus_hv_solver_id == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::fillYbus: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (hv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }
        int bus_lv_id_me = bus_lv_id_(trafo_id);
        int bus_lv_solver_id = id_grid_to_solver[bus_lv_id_me];
        if(bus_lv_solver_id == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::fillYbus: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (lv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }

        // TODO time optim all that could be done once and for all
        // subsecptance
        cplx_type h = 0.;
        if(ac){
            h = h_(trafo_id);
            h = my_i * my_half_ * h;
        }
        // admittance
        cplx_type y = 0.;
        cplx_type z = x_(trafo_id);
        if(ac){
            z *= my_i;
            z += r_(trafo_id);  // r_ is the resistance, not the ratio !
        }
        if(z != my_zero_) y = my_one_ / z;
        // END todo

        // get the transformers ratio
        real_type ratio = ratio_(trafo_id);
        real_type alpha = shift_(trafo_id);
        cplx_type eialpha  = {my_one_, my_zero_};  // exp(j  * alpha)
        cplx_type eimalpha = {my_one_, my_zero_};  // exp(-j * alpha)
        if(alpha != 0.)
        {
            real_type cos_theta = std::cos(alpha);
            real_type sin_theta = std::sin(alpha);
            eialpha = {cos_theta, sin_theta};
            eimalpha = {cos_theta, -sin_theta};
        }

        // fill non diagonal coefficient
        if(!ac){
            // dc mode
            // ratio = my_one_; // in dc, ratio = 1.0 here (same voltage both side)
            eialpha = my_one_;
            eimalpha = my_one_;
        }
        if(!is_tap_hv_side_[trafo_id]) ratio = my_one_ / ratio;
        cplx_type tmp = y / ratio;  // here ratio should not be 1.0 even in dc mode
        res.push_back(Eigen::Triplet<cplx_type> (bus_hv_solver_id, bus_lv_solver_id, -tmp * eialpha));
        res.push_back(Eigen::Triplet<cplx_type> (bus_lv_solver_id, bus_hv_solver_id, -tmp * eimalpha));

        // fill diagonal coefficient
        if(!ac)
        {
            // tmp = y;  // i cancel the effect of the ratio here (same both side) ony for diagonal coeff
            ratio = my_one_;
        }
        if(ac) tmp += h;
        // else tmp += std::imag(h);  // todo ???? still don't know !
        res.push_back(Eigen::Triplet<cplx_type>(bus_hv_solver_id, bus_hv_solver_id, tmp / ratio));
        res.push_back(Eigen::Triplet<cplx_type>(bus_lv_solver_id, bus_lv_solver_id, tmp * ratio));

    }
}

void DataTrafo::fillSbus(CplxVect & Sbus, bool ac, const std::vector<int> & id_grid_to_solver){
    if(ac) return;
    int nb_trafo = nb();
    int bus_id_me, bus_id_solver_hv, bus_id_solver_lv;
    cplx_type tmp;
    for(int trafo_id = 0; trafo_id < nb_trafo; ++trafo_id){
        //  i don't do anything if the load is disconnected
        if(!status_[trafo_id]) continue;

        double shift = shift_[trafo_id];
        if(shift == 0.) continue;

        double ratio = ratio_[trafo_id];
        if(!is_tap_hv_side_[trafo_id]) ratio = my_one_ / ratio;
        tmp = shift / x_[trafo_id] / ratio;

        bus_id_me = bus_lv_id_(trafo_id);
        bus_id_solver_lv = id_grid_to_solver[bus_id_me];
        if(bus_id_solver_lv == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::fillSbus: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (hv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }
        bus_id_me = bus_hv_id_(trafo_id);
        bus_id_solver_hv = id_grid_to_solver[bus_id_me];
        if(bus_id_solver_hv == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::fillSbus: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (lv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }

        Sbus.coeffRef(bus_id_solver_hv) += tmp;
        Sbus.coeffRef(bus_id_solver_lv) -= tmp;
    }
}

void DataTrafo::compute_results(const Eigen::Ref<const RealVect> & Va,
                                const Eigen::Ref<const RealVect> & Vm,
                                const Eigen::Ref<const CplxVect> & V,
                                const std::vector<int> & id_grid_to_solver,
                                const RealVect & bus_vn_kv,
                                real_type sn_mva
                                )
{
    // it needs to be initialized at 0.
    int nb_element = nb();
    res_p_hv_ = RealVect::Constant(nb_element, 0.0);  // in MW
    res_q_hv_ = RealVect::Constant(nb_element, 0.0);  // in MVar
    res_v_hv_ = RealVect::Constant(nb_element, 0.0);  // in kV
    res_a_hv_ = RealVect::Constant(nb_element, 0.0);  // in kA
    res_p_lv_ = RealVect::Constant(nb_element, 0.0);  // in MW
    res_q_lv_ = RealVect::Constant(nb_element, 0.0);  // in MVar
    res_v_lv_ = RealVect::Constant(nb_element, 0.0);  // in kV
    res_a_lv_ = RealVect::Constant(nb_element, 0.0);  // in kA
    res_theta_hv_ = RealVect::Constant(nb_element, 0.0);  // in degree
    res_theta_lv_ = RealVect::Constant(nb_element, 0.0);  // in degree
    for(int trafo_id = 0; trafo_id < nb_element; ++trafo_id){
        // don't do anything if the element is disconnected
        if(!status_[trafo_id]) continue;

        //physical properties
        real_type r = r_(trafo_id);
        real_type x = x_(trafo_id);
        real_type ratio_me = ratio_(trafo_id);
        cplx_type h = my_i * my_half_ * h_(trafo_id);
        cplx_type y = my_one_ / (r + my_i * x);

        if(!is_tap_hv_side_[trafo_id])
        {
            // tap is lv side i need to change it
            ratio_me = my_one_ / ratio_me;
        }
        y /= ratio_me;

        real_type alpha = shift_(trafo_id);
        cplx_type eialpha  = {my_one_, my_zero_};  // exp(j  * alpha)
        cplx_type eimalpha = {my_one_, my_zero_};  // exp(-j * alpha)
        if(alpha != 0.)
        {
            real_type cos_theta = std::cos(alpha);
            real_type sin_theta = std::sin(alpha);
            eialpha = {cos_theta, sin_theta};
            eimalpha = {cos_theta, -sin_theta};
        }

        // connectivity
        int bus_hv_id_me = bus_hv_id_(trafo_id);
        int bus_hv_solver_id = id_grid_to_solver[bus_hv_id_me];
        if(bus_hv_solver_id == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::compute_results: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (hv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }
        int bus_lv_id_me = bus_lv_id_(trafo_id);
        int bus_lv_solver_id = id_grid_to_solver[bus_lv_id_me];
        if(bus_lv_solver_id == _deactivated_bus_id){
            std::ostringstream exc_;
            exc_ << "DataTrafo::compute_results: the trafo with id ";
            exc_ << trafo_id;
            exc_ << " is connected (lv side) to a disconnected bus while being connected";
            throw std::runtime_error(exc_.str());
        }

        // results of the powerflow
        cplx_type Ehv = V(bus_hv_solver_id);
        cplx_type Elv = V(bus_lv_solver_id);

        // powerline equations
        cplx_type I_hvlv =  (y + h) / ratio_me * Ehv - y * eialpha * Elv ;
        cplx_type I_lvhv = (y + h) * ratio_me * Elv - y * eimalpha * Ehv;

        I_hvlv = std::conj(I_hvlv);
        I_lvhv = std::conj(I_lvhv);
        cplx_type s_hvlv = Ehv * I_hvlv;
        cplx_type s_lvhv = Elv * I_lvhv;

        res_p_hv_(trafo_id) = std::real(s_hvlv) * sn_mva;
        res_q_hv_(trafo_id) = std::imag(s_hvlv) * sn_mva;
        res_p_lv_(trafo_id) = std::real(s_lvhv) * sn_mva;
        res_q_lv_(trafo_id) = std::imag(s_lvhv) * sn_mva;

        // retrieve voltages magnitude in kv instead of pu
        real_type v_hv = Vm(bus_hv_solver_id);
        real_type v_lv = Vm(bus_lv_solver_id);
        real_type bus_vn_kv_hv = bus_vn_kv(bus_hv_id_me);
        real_type bus_vn_kv_lv = bus_vn_kv(bus_lv_id_me);
        res_v_hv_(trafo_id) = v_hv * bus_vn_kv_hv;
        res_v_lv_(trafo_id) = v_lv * bus_vn_kv_lv;

        res_theta_hv_(trafo_id) = Va(bus_hv_solver_id) * 180. / my_pi;
        res_theta_lv_(trafo_id) = Va(bus_lv_solver_id) * 180. / my_pi;

    }
    _get_amps(res_a_hv_, res_p_hv_, res_q_hv_, res_v_hv_);
    _get_amps(res_a_lv_, res_p_lv_, res_q_lv_, res_v_lv_);
}

void DataTrafo::reset_results(){
    res_p_hv_ = RealVect();  // in MW
    res_q_hv_ = RealVect();  // in MVar
    res_v_hv_ = RealVect();  // in kV
    res_a_hv_ = RealVect();  // in kA
    res_p_lv_ = RealVect();  // in MW
    res_q_lv_ = RealVect();  // in MVar
    res_v_lv_ = RealVect();  // in kV
    res_a_lv_ = RealVect();  // in kA
}

real_type DataTrafo::get_p_slack(int slack_bus_id)
{
    int nb_element = nb();
    real_type res = 0.;
    for(int line_id = 0; line_id < nb_element; ++line_id)
    {
        if(!status_[line_id]) continue;
        if(bus_hv_id_(line_id) == slack_bus_id) res += res_p_hv_(line_id);
        if(bus_lv_id_(line_id) == slack_bus_id) res += res_p_lv_(line_id);
    }
    return res;
}

void DataTrafo::get_q(std::vector<real_type>& q_by_bus)
{
    int nb_element = nb();
    for(int el_id = 0; el_id < nb_element; ++el_id)
    {
        if(!status_[el_id]) continue;
        int bus_id_hv = bus_hv_id_[el_id];
        int bus_id_lv = bus_lv_id_[el_id];
        q_by_bus[bus_id_hv] += res_q_hv_(el_id);
        q_by_bus[bus_id_lv] += res_q_lv_(el_id);
    }
}
