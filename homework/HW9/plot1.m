function [fitresult, gof] = plot1(w_num, t_w)
%CREATEFIT(W_NUM,T_W)
%  Create a fit.
%
%  Data for 'untitled fit 1' fit:
%      X Input : w_num
%      Y Output: t_w
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 18-Nov-2020 20:22:01 自动生成


%% Fit: 'untitled fit 1'.
[xData, yData] = prepareCurveData( w_num, t_w );

% Set up fittype and options.
ft = fittype( 'poly1' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft );

% Plot fit with data.
figure( 'Name', 'untitled fit 1' );
plot( fitresult, xData, yData );
% Label axes
xlabel('the number of edges')
ylabel('t')
% xlabel( 'w_num', 'Interpreter', 'none' );
% ylabel( 't_w', 'Interpreter', 'none' );
grid on


